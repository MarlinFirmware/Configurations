#!/usr/bin/env python3
"""
check_tramming_inset.py

Check BED_TRAMMING_INSET_LFRB in every example configuration and,
with --fix, raise any inset that is too small to the smallest valid value.

An inset is valid when the config still builds and the tramming points can
be reached after the user enables LCD_BED_TRAMMING, and also
BED_TRAMMING_USE_PROBE when the config has a bed probe.

  - Nozzle: every tramming point lies inside X/Y_MIN_POS..X/Y_MAX_POS
    (inside PRINTABLE_RADIUS on kinematic machines; only deltas are
    fixed automatically, SCARA/TPARA are reported).
    Configs whose travel limits miss the bed by more than a quarter of its
    size are reported but not changed, since the bed position is the fault.
  - Probe: the static_assert in menu_bed_tramming.cpp passes. Each edge of
    the tramming rectangle must be reachable by the probe at its default
    NOZZLE_TO_PROBE_OFFSET with PROBING_MARGIN applied. Not checked for
    SENSORLESS_PROBING, which can't be used with BED_TRAMMING_USE_PROBE.

Values are evaluated by compiling a small program against Marlin's own
configuration headers, so expressions and Conditionals are resolved
exactly as in a real build.

Usage:
  bin/check_tramming_inset.py --marlin /path/to/Marlin [--fix] [path ...]

  --marlin  Marlin source tree (the directory containing Marlin/src),
            ideally a clean checkout of the matching bugfix branch.
  path      Config folders or Configuration.h files to check.
            Default: config/
"""

import argparse, math, re, shutil, subprocess, sys, tempfile
from pathlib import Path

FSLOP = 0.0001

# Configs that select a model with a -D from Marlin's PlatformIO env.
# The inset must suit every model, so each one is checked.
VARIANTS = {
  'Alfawise/U20': ['U20', 'U20_PLUS', 'U30', 'LK1', 'LK1_PLUS', 'LK2', 'LK4'],
  'Alfawise/U20-bltouch': ['U20', 'U20_PLUS', 'U30', 'LK1', 'LK1_PLUS', 'LK2', 'LK4'],
}

def variants_for(cfg):
  key = cfg.as_posix().split('config/examples/')[-1]
  return [[d] for d in VARIANTS.get(key, [])] or [[]]

CHECK_CPP = r'''
#include <cmath>
#define sq(x) ((x)*(x))
#include "inc/MarlinConfigPre.h"
#include "inc/Conditionals-5-post.h"
#include <cstdio>
int main() {
  constexpr float i[4] = BED_TRAMMING_INSET_LFRB;
  printf("inset %f %f %f %f\n", i[0], i[1], i[2], i[3]);
  printf("bed %f %f %f %f\n", double(X_MIN_BED), double(Y_MIN_BED), double(X_MAX_BED), double(Y_MAX_BED));
  printf("center %f %f\n", double(X_CENTER), double(Y_CENTER));
  printf("pos %f %f %f %f\n", double(X_MIN_POS), double(Y_MIN_POS), double(X_MAX_POS), double(Y_MAX_POS));
  printf("margin %f %f %f %f\n", double(PROBING_MARGIN_LEFT), double(PROBING_MARGIN_FRONT), double(PROBING_MARGIN_RIGHT), double(PROBING_MARGIN_BACK));
  #if IS_KINEMATIC && defined(PRINTABLE_RADIUS)
    printf("kinematic %f\n", double(PRINTABLE_RADIUS));
    printf("delta %d\n", ENABLED(DELTA));
    #ifdef PROBING_MARGIN
      printf("kmargin %f\n", double(PROBING_MARGIN));
    #endif
  #endif
  #if HAS_BED_PROBE && DISABLED(SENSORLESS_PROBING)
    constexpr float o[] = NOZZLE_TO_PROBE_OFFSET;
    printf("probe %f %f\n", o[0], o[1]);
  #endif
}
'''

INSET_RE = re.compile(r'^(\s*(?://\s*)?#define\s+BED_TRAMMING_INSET_LFRB\s+)\{([^}]*)\}(\s*)(//.*)?$')

class Checker:
  def __init__(self, marlin):
    self.tmp = Path(tempfile.mkdtemp(prefix='tramming_'))
    src = Path(marlin) / 'Marlin' / 'src'
    if not (src / 'inc' / 'MarlinConfigPre.h').exists():
      sys.exit(f"No Marlin source at {src}")
    self.mdir = self.tmp / 'Marlin'
    shutil.copytree(src, self.mdir / 'src')
    (self.tmp / 'check.cpp').write_text(CHECK_CPP)

  def cleanup(self):
    shutil.rmtree(self.tmp, ignore_errors=True)

  def evaluate(self, cfg_dir, conf_text=None, defines=()):
    """Compile and run the probe program for one config. Return a dict of values."""
    for name in ('Configuration.h', 'Configuration_adv.h'):
      f = cfg_dir / name
      text = conf_text if (name == 'Configuration.h' and conf_text is not None) else f.read_text(errors='replace')
      # Drop #error lines: the import-branch guard, and model pickers (e.g. Alfawise)
      # that expect a -D from the build environment. Only the values matter here.
      text = re.sub(r'^\s*#\s*error\b.*$', '', text, flags=re.M)
      (self.mdir / name).write_text(text)
    exe = self.tmp / 'check'
    r = subprocess.run(['g++', '-std=gnu++17', '-w', '-D__MARLIN_DEPS__', '-DLCD_BED_TRAMMING=', '-DNO_CONTROLLER_CUSTOM_WIRING_WARNING',
                        *[f'-D{d}' for d in defines],
                        f'-I{self.mdir / "src"}', '-o', str(exe), str(self.tmp / 'check.cpp'), '-lm'],
                       capture_output=True, text=True)
    if r.returncode:
      err = next((l for l in r.stderr.splitlines() if 'error' in l), r.stderr.strip()[:200])
      raise RuntimeError(err)
    out = subprocess.run([str(exe)], capture_output=True, text=True, check=True).stdout
    v = {}
    for line in out.splitlines():
      k, *nums = line.split()
      v[k] = [float(n) for n in nums]
    return v

def required_insets(v):
  """Smallest valid inset for each side (L, F, R, B), with the reason for each."""
  xmin, ymin, xmax, ymax = v['bed']
  req = [(-math.inf, '')] * 4

  def need(i, val, why):
    if val > req[i][0]: req[i] = (val, why)

  if 'kinematic' in v:
    radius = v['kinematic'][0]
    xc, yc = v['center']
    # Nozzle: all four corners inside the printable radius (only fixed for square-symmetric cases)
    # Probe: edge midpoints inside the probe radius, as in menu_bed_tramming.cpp
    if 'probe' in v:
      ox, oy = v['probe']
      pr = radius - max(v.get('kmargin', [0])[0], math.hypot(ox, oy))
      hx = math.sqrt(max(pr * pr - yc * yc, 0))
      hy = math.sqrt(max(pr * pr - xc * xc, 0))
      need(0, -hx - xmin, 'probe radius')
      need(2, xmax - hx, 'probe radius')
      need(1, -hy - ymin, 'probe radius')
      need(3, ymax - hy, 'probe radius')
  else:
    pxmin, pymin, pxmax, pymax = v['pos']
    need(0, pxmin - xmin, 'X_MIN_POS')
    need(1, pymin - ymin, 'Y_MIN_POS')
    need(2, xmax - pxmax, 'X_MAX_POS')
    need(3, ymax - pymax, 'Y_MAX_POS')
    if 'probe' in v:
      ox, oy = v['probe']
      ml, mf, mr, mb = v['margin']
      need(0, max(ml, pxmin + ox - xmin), 'probe')
      need(1, max(mf, pymin + oy - ymin), 'probe')
      need(2, max(mr, xmax - (pxmax + ox)), 'probe')
      need(3, max(mb, ymax - (pymax + oy)), 'probe')
  return req

def corners_outside(v, inset):
  """Tramming corners outside PRINTABLE_RADIUS on a kinematic machine."""
  if 'kinematic' not in v: return []
  radius = v['kinematic'][0]
  xmin, ymin, xmax, ymax = v['bed']
  lf = (xmin + inset[0], ymin + inset[1]); rb = (xmax - inset[2], ymax - inset[3])
  corners = { 'LF': lf, 'RF': (rb[0], lf[1]), 'RB': rb, 'LB': (lf[0], rb[1]) }
  return [n for n, (x, y) in corners.items() if math.hypot(x, y) > radius + FSLOP]

def fix_corners(v, inset):
  """Delta: raise insets to a common minimum until every corner is inside PRINTABLE_RADIUS."""
  if not corners_outside(v, inset): return inset
  lo, hi = 0.0, max(v['bed'][2] - v['bed'][0], v['bed'][3] - v['bed'][1]) / 2
  if corners_outside(v, [max(i, hi) for i in inset]): return None
  for _ in range(60):
    mid = (lo + hi) / 2
    if corners_outside(v, [max(i, mid) for i in inset]): lo = mid
    else: hi = mid
  t = math.ceil(hi - FSLOP)
  return [max(i, t) for i in inset]

def travel_mismatch(v):
  """
  Travel limits that miss a bed edge by more than a quarter of the bed mean
  the bed position itself is wrong (e.g., BED_CENTER_AT_0_0 vs. X_MIN_POS).
  Raising the inset would only hide that, so these are left for a human.
  """
  if 'kinematic' in v: return []
  xmin, ymin, xmax, ymax = v['bed']
  pxmin, pymin, pxmax, pymax = v['pos']
  qx, qy = (xmax - xmin) / 4, (ymax - ymin) / 4
  out = []
  if pxmin - xmin > qx: out.append(f"X_MIN_POS {pxmin:g} vs bed left {xmin:g}")
  if xmax - pxmax > qx: out.append(f"X_MAX_POS {pxmax:g} vs bed right {xmax:g}")
  if pymin - ymin > qy: out.append(f"Y_MIN_POS {pymin:g} vs bed front {ymin:g}")
  if ymax - pymax > qy: out.append(f"Y_MAX_POS {pymax:g} vs bed back {ymax:g}")
  return out

def fmt_num(x):
  return str(int(x)) if float(x).is_integer() else f'{x:g}'

def rewrite_line(text, new_vals):
  lines = text.split('\n')
  for n, line in enumerate(lines):
    m = INSET_RE.match(line)
    if not m: continue
    head, _, gap, comment = m.groups()
    body = head + '{ ' + ', '.join(new_vals) + ' }'
    if comment:
      col = len(head) + len(m.group(2)) + 2 + len(gap)  # original comment column
      body = body.ljust(col - 1) + ' ' + comment if len(body) < col else body + ' ' + comment
    lines[n] = body
    return '\n'.join(lines), n + 1
  return None, None

def analyse(v):
  """
  Check one evaluated config.
  Return (new_insets, reasons, problem). problem is set when it needs a human.
  """
  inset = v['inset']
  mismatch = travel_mismatch(v)
  if mismatch:
    return None, [], f"travel limits don't match the bed ({'; '.join(mismatch)}). Fix by hand."

  req = required_insets(v)
  new = list(inset)
  reasons = []
  for i, side in enumerate('LFRB'):
    r, why = req[i]
    if inset[i] < r - FSLOP:
      new[i] = math.ceil(r - FSLOP)
      reasons.append(f"{side} {fmt_num(inset[i])} < {r:g} ({why})")

  corners = corners_outside(v, new)
  if corners:
    reasons.append(f"corners {', '.join(corners)} outside PRINTABLE_RADIUS {v['kinematic'][0]:g}")
    # SCARA/TPARA reach isn't a simple disk, so only deltas are fixed
    fixed_new = fix_corners(v, new) if v['delta'][0] else None
    if fixed_new is None:
      return None, reasons, "Fix by hand."
    new = fixed_new
  return new, reasons, None

def main():
  ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
  ap.add_argument('--marlin', required=True, help='Marlin source tree (contains Marlin/src)')
  ap.add_argument('--fix', action='store_true', help='Rewrite incorrect insets')
  ap.add_argument('paths', nargs='*', default=['config'])
  args = ap.parse_args()

  confs = []
  for p in map(Path, args.paths):
    confs += [p] if p.is_file() else sorted(p.rglob('Configuration.h'))
  confs = [c for c in confs if 'BED_TRAMMING_INSET_LFRB' in c.read_text(errors='replace')]

  chk = Checker(args.marlin)
  bad = errors = fixed = 0

  def check(cfg, text=None):
    """Analyse every variant. Return (inset, new, reasons, problem)."""
    inset, new, reasons, problem = None, None, [], None
    for defs in variants_for(cfg):
      v = chk.evaluate(cfg, text, defs)
      tag = f"[{defs[0]}] " if defs else ''
      n, r, pr = analyse(v)
      inset = v['inset']
      reasons += [tag + x for x in r]
      if pr: problem = tag + pr
      elif n: new = n if new is None else [max(a, b) for a, b in zip(new, n)]
    return inset, new, reasons, problem

  try:
    for conf in confs:
      cfg = conf.parent
      try:
        inset, new, reasons, problem = check(cfg)
      except RuntimeError as e:
        errors += 1
        print(f"ERROR {cfg}: {e}")
        continue
      if not reasons and not problem: continue

      bad += 1
      print(f"{cfg}: {{ {', '.join(map(fmt_num, inset))} }}")
      for r in reasons: print(f"    {r}")
      if problem:
        print(f"    {problem}")
        continue
      print(f"    -> {{ {', '.join(map(fmt_num, new))} }}")

      if args.fix:
        text = conf.read_text()
        newtext, lineno = rewrite_line(text, [fmt_num(x) for x in new])
        if newtext is None:
          print("    could not find the define line to rewrite")
          continue
        # Confirm the rewritten file evaluates clean before saving it
        _, _, r2, p2 = check(cfg, newtext)
        if r2 or p2:
          print("    rewrite did not validate; left unchanged")
          continue
        conf.write_text(newtext)
        fixed += 1
        print(f"    fixed (line {lineno})")
  finally:
    chk.cleanup()

  print(f"\nChecked {len(confs)} configs: {bad} incorrect, {fixed} fixed, {errors} could not be evaluated.")
  return 1 if (bad - fixed) or errors else 0

if __name__ == '__main__':
  sys.exit(main())
