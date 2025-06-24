# Overview
This configuration is built and tested for the MakerGear M2 Revision H. I will try to note obvious differences in the other revisions to help support them. Some of the original firmwares notes are incorrect but many of the details are available here - https://makergear.zendesk.com/hc/en-us/articles/360022528292

# Z Max Homing on Rev F, G, H
Revision E moved the Z endstop switch to the bottom/max. For all other revisions set `Z_HOME_DIR` to -1 for Z Min Homing. This is not a common configuration and certain unexpected behaviours may occur. The primary solution has been to move off the endstop by 5mm with `HOMING_BACKOFF_POST_MM`. This mitigates the current Bed Tramming routine moving down by `BED_TRAMMING_Z_HOP` which defaults to 4 and does not respect Z_MAX_POS. 

### Warnings
If the bed is left all the way up. Take care when doing things like loading filament immediately after powering on the printer. With Z Max homing the printer will not lower the bed because it may be at Z Max but it will raise it after. This raise/lower prior to homing can be eliminated with `NO_MOTION_BEFORE_HOMING` at the cost of being able to jog the motors while not homed. Prior revisions have the opposite and/or less of a problem. They will lower the bed (even if all the way down) and raise after.

## Motor / Endstop / Pulley Changes
### Endstops
 - Rev F, G, and H are Normally Closed (Hit State HIGH)
 - Earlier Revisions are Normally Open (Hit State LOW)
   
### Z Motor
 - Black Motors on Rev F, G, and H require `INVERT_Z_DIR true`.
 - Black Motors on Rev C.1, D, D.1, E and E.1 should be false.
 - Silver Motors on older revisions should be true.
   
### Extruder Motor
 - INVERT_E0_DIR false for Rev F, G and H
 - Previous revisions are currently unclear but likely set to true.

### Steps Per MM Changes
 - Revision G and H use 16 tooth pulley specifed as 80.1
 - Prior Revisions use 18 tooth pulley specified as 88.88 or 88.89
 - Silver Z Motors are T8x8 specified at 400
 - Black Z Motors are Imperial 1/8" specified at 1007.7 

# Hotends
Specified operating temperatures by version. Firmware maximums were typically plus overshoot.
 - v3a - 220ºC
 - v3b - 250ºC
 - v4 - 290ºC 

# Setting Distance Between Nozzle and Bed
Most revisions use M206 to set the nozzle distance from the bed. Z Max homed revisions will be a slighty different experience from Z Min homing. I have set the Z Max to 210 which on my Rev H puts the nozzle a little over 1mm from the bed before dialing this in. My printer currently as an example has M206 Z1.2 set. If I changed Z_MAX_POS to 200 I would have to do M206 Z11.2 instead.

### Basic Guide
 - Power on the Printer
 - Connect Pronterface first as it will reset the printer
 - Home `G28`
 - Move X and Y to Bed Center `G1 F4000 X100 Y150`
 - Move Z Up to 0, You can be careful but not going all the way at first.
   - First Move very close `G1 F1800 Z5`
   - Slowly move the rest of the way `G1 F100 Z0`
 - At this point your nozzle probably is not close to the bed at all. Measure or take your first guess at how much closer you need to be.
   - Enter this first attempt lets say 1mm with `M206 Z1`
   - Home `G28` and move back to check the adjustment `G1 F4000 X100 Y150 Z0`
   - Adjust again for example .2 mm closer enter the full amount total `M206 Z1.2`
   - Rinse and Repeat the last 2 steps until you feel ready to test printing
 - Saved the setting with `M500`

If the printer's bed is not trammed I would tram it now under Probe & Level. During the first test print double click the screen knob to activate baby stepping. If you find you need further adjustment for example we moved +.05 away from the bed to make it just right you can later adjust your M206 value from 1.2 to 1.25. Don't forget to save. 
