# MakerGear M2 Rev.H

## Overview
This configuration is built and tested for the MakerGear M2 Revision H. I will note obvious differences in the other revisions to help support them. Some of the original firmware's notes are incorrect, but many of the details are available [here](//makergear.zendesk.com/hc/en-us/articles/360022528292).

## Z Max Homing on Rev F, G, H
Revision E moved the Z end‑stop switch to the bottom (max). For all other revisions set `Z_HOME_DIR` to –1 for Z‑min homing. This is not a common configuration, and certain unexpected behaviors may occur. The primary solution has been to move off the end‑stop by 5mm with `HOMING_BACKOFF_POST_MM`. This mitigates the current Bed Tramming routine moving down by `BED_TRAMMING_Z_HOP`, which defaults to 4mm and does not respect `Z_MAX_POS`.

### Warnings
If the bed is left all the way up, take care when loading filament immediately after powering on the printer. With Z‑Max homing the printer will not lower the bed because it may be at Z‑Max, but it will raise it after. This raise/lower prior to homing can be eliminated with `NO_MOTION_BEFORE_HOMING` at the cost of being able to jog the motors while not homed. Prior revisions have the opposite and/or less of a problem. They will lower the bed (even if all the way down) and raise after.

## Motor / Endstop / Pulley Changes

### Endstops
- Rev F, G, and H are normally closed (hit state `HIGH`).
- Earlier revisions are normally open (hit state `LOW`).

### Z Motor
- Black motors on Rev F, G, and H require `INVERT_Z_DIR true`.
- Black motors on Rev C.1, D, D.1, E, and E.1 should be set to false.
- Silver motors on older revisions should be true.

### Extruder Motor
- `INVERT_E0_DIR false` for Rev F, G, and H.
- Previous revisions are currently unclear but likely set to true.

### Steps Per MM Changes
- Rev G and H use a 16‑tooth pulley specified as 80.1.
- Prior revisions use an 18‑tooth pulley specified as 88.88 or 88.89.
- Silver Z motors are T8×8 specified at 400.
- Black Z motors are Imperial 1/8" specified at 1007.7.

## Hotends
Operating temperatures by version (typical firmware maximum plus overshoot).
- v3a – 220°C
- v3b – 250°C
- v4 – 290°C

## Setting the Distance Between Nozzle and Bed
Most revisions use `M206` to set the nozzle distance from the bed. Z‑Max homed revisions will experience a slightly different workflow from Z‑Min homing. I set the Z‑Max to 210, which on my Rev H places the nozzle just over 1mm from the bed before dialing this in. My printer currently has `M206 Z1.2` set. If I changed `Z_MAX_POS` to 200, I would need to set `M206 Z11.2` instead.

### Basic Guide
1. Power on the printer.
2. Connect Pronterface first; it will reset the printer.
3. Home with `G28`.
4. Move X and Y to the bed center: `G1 F4000 X100 Y150`.
5. Move Z up to 0. Be careful not to go all the way at first.
   - Move very close: `G1 F1800 Z5`.
   - Move the rest of the way: `G1 F100 Z0`.
6. At this point your nozzle probably isn't close to the bed at all. Measure or guess how much closer you need to be.
   - For a first attempt of 1mm, enter `M206 Z1`.
   - Home with `G28` and move back to check the adjustment: `G1 F4000 X100 Y150 Z0`.
   - Adjust again, e.g., 0.2mm closer, by entering the full amount total: `M206 Z1.2`.
   - Repeat the last two steps until you're ready to test print.
7. Save the setting with `M500`.

If the printer's bed is not trammed, tram it now under **Probe & Level**. During the first test print double‑click the screen knob to activate baby stepping. If you find you need further adjustment—for example, you moved +0.05mm away from the bed to make it just right—you can later adjust your `M206` value from 1.2 to 1.25. Don't forget to save.
