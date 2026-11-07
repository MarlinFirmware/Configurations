#!/usr/bin/env python3
"""
Tests for bin/mfsync.

Builds a small fake Configurations repo in a temp dir and checks that
mfsync finds examples that missed a change to config/default, in both
directions, and that --fix applies the missed text changes.

Run:  python3 bin/test_mfsync.py
"""
import os
import sys
import shutil
import tempfile
import subprocess
import importlib.machinery
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
mfsync = importlib.machinery.SourceFileLoader('mfsync', str(ROOT / 'bin' / 'mfsync')).load_module()

# A default with a change: a comment line is added and an option is enabled
OLD_DEF = """// @section serial
#define SERIAL_PORT 0
//#define HOST_ACTION_COMMANDS
#define BAUDRATE 250000
"""
NEW_DEF = """// @section serial
#define SERIAL_PORT 0
#define HOST_ACTION_COMMANDS
// A new comment line
#define BAUDRATE 250000
"""

# An example that has the change (new text, option enabled)
GOOD = """// @section serial
#define SERIAL_PORT 0
#define HOST_ACTION_COMMANDS
// A new comment line
#define BAUDRATE 250000
"""
# An example that missed it (old text, option still disabled)
STALE = """// @section serial
#define SERIAL_PORT 0
//#define HOST_ACTION_COMMANDS
#define BAUDRATE 250000
"""


def run(root, *args):
    return subprocess.run(('python3', str(ROOT / 'bin' / 'mfsync')) + args,
                          cwd=root, capture_output=True, text=True)


def make_repo():
    tmp = Path(tempfile.mkdtemp(prefix='mfsync-test-'))
    subprocess.run(('git', 'init', '-q', '-b', 'import-2.1.x', str(tmp)), check=True)
    subprocess.run(('git', '-C', str(tmp), 'config', 'user.email', 't@t'), check=True)
    subprocess.run(('git', '-C', str(tmp), 'config', 'user.name', 't'), check=True)
    return tmp


def write(root, rel, text):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')


def commit(root, msg):
    subprocess.run(('git', '-C', str(root), 'add', '-A'), check=True)
    subprocess.run(('git', '-C', str(root), 'commit', '-q', '-m', msg), check=True)


def test_detection():
    tmp = make_repo()
    try:
        # Base: default and two examples, all with the OLD text
        write(tmp, 'config/default/Configuration.h', OLD_DEF)
        write(tmp, 'config/examples/Good/Configuration.h', OLD_DEF)
        write(tmp, 'config/examples/Stale/Configuration.h', OLD_DEF)
        commit(tmp, 'base')
        base = subprocess.run(('git', '-C', str(tmp), 'rev-parse', 'HEAD'),
                              capture_output=True, text=True).stdout.strip()

        # A PR that updates the default and the Good example, but not Stale
        write(tmp, 'config/default/Configuration.h', NEW_DEF)
        write(tmp, 'config/examples/Good/Configuration.h', GOOD)
        commit(tmp, 'pr')
        head = subprocess.run(('git', '-C', str(tmp), 'rev-parse', 'HEAD'),
                              capture_output=True, text=True).stdout.strip()

        # PR mode: the PR's change must reach every example
        r = run(tmp, '--pr', '--base', base, '--head', head)
        assert 'Stale' in r.stdout and 'Good' not in r.stdout, r.stdout
        assert 'A new comment line' in r.stdout, r.stdout
        assert r.returncode == 1, r.returncode

        # --since mode on the working tree
        r = run(tmp, '--since', base)
        assert 'Stale' in r.stdout and 'Good' not in r.stdout, r.stdout
        assert r.returncode == 1, r.returncode

        # --fix applies the text change to Stale
        r = run(tmp, '--since', base, '--fix')
        assert 'Fixed: config/examples/Stale/Configuration.h' in r.stdout, r.stdout
        assert 'HOST_ACTION_COMMANDS' in (tmp / 'config/examples/Stale/Configuration.h').read_text()
        # The setting change is not applied without --settings
        assert '//#define HOST_ACTION_COMMANDS' in (tmp / 'config/examples/Stale/Configuration.h').read_text()

        # Recheck is clean
        r = run(tmp, '--since', base)
        assert r.returncode == 0, r.stdout
        print('test_detection: OK')
    finally:
        shutil.rmtree(tmp)


def test_settings():
    # A setting-only change. An example added to the base after the PR
    # branched can't have got it, so it is an error in --pr mode.
    tmp = make_repo()
    try:
        SET_DEF = OLD_DEF.replace('//#define HOST_ACTION_COMMANDS', '#define HOST_ACTION_COMMANDS')
        write(tmp, 'config/default/Configuration.h', OLD_DEF)
        commit(tmp, 'base0')
        git = lambda *a: subprocess.run(('git', '-C', str(tmp)) + a, check=True, capture_output=True, text=True).stdout.strip()
        git('checkout', '-q', '-b', 'pr')
        write(tmp, 'config/default/Configuration.h', SET_DEF)
        commit(tmp, 'pr')
        git('checkout', '-q', 'import-2.1.x')
        write(tmp, 'config/examples/New/Configuration.h', OLD_DEF)
        commit(tmp, 'new example')
        base = git('rev-parse', 'HEAD')

        r = run(tmp, '--pr', '--base', base, '--head', 'pr')
        assert 'config/examples/New/Configuration.h' in r.stdout, r.stdout
        assert 'HOST_ACTION_COMMANDS' in r.stdout, r.stdout
        assert r.returncode == 1, r.returncode

        # Merge the PR: --since lists the setting for review, not as an error
        git('merge', '-q', '--no-edit', 'pr')
        r = run(tmp, '--since', base)
        assert '[review]' in r.stdout, r.stdout
        assert r.returncode == 0, r.returncode

        # --strict makes it an error
        r = run(tmp, '--since', base, '--strict')
        assert r.returncode == 1, r.returncode

        # --fix --settings applies it
        r = run(tmp, '--since', base, '--fix', '--settings')
        assert 'Fixed: config/examples/New/Configuration.h' in r.stdout, r.stdout
        assert '\n#define HOST_ACTION_COMMANDS' in (tmp / 'config/examples/New/Configuration.h').read_text()
        print('test_settings: OK')
    finally:
        shutil.rmtree(tmp)


def test_comment_only_change():
    # A change that only touches a comment must still be caught
    tmp = make_repo()
    try:
        write(tmp, 'config/default/Configuration.h', OLD_DEF)
        write(tmp, 'config/examples/Stale/Configuration.h', OLD_DEF)
        commit(tmp, 'base')
        base = subprocess.run(('git', '-C', str(tmp), 'rev-parse', 'HEAD'),
                              capture_output=True, text=True).stdout.strip()
        write(tmp, 'config/default/Configuration.h', NEW_DEF)
        commit(tmp, 'pr')
        r = run(tmp, '--since', base)
        assert 'Stale' in r.stdout, r.stdout
        assert r.returncode == 1, r.returncode
        print('test_comment_only_change: OK')
    finally:
        shutil.rmtree(tmp)


if __name__ == '__main__':
    test_detection()
    test_settings()
    test_comment_only_change()
    print('All mfsync tests passed.')
