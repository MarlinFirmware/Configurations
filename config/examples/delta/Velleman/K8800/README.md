# Velleman Vertex Delta K8800

**PLEASE READ THE WARNINGS SECTION CAREFULLY, ESPECIALLY IF YOU INTEND TO USE UBL.**

## Introduction

This configuration is for the Velleman Vertex Delta K8800. It was derived by Stephen Parry:

- sgparry@mainscreen.com
- stephen@EduMake.org

It is based both on the original Velleman stock firmware, derived from Marlin 1.1.4, and work by SusisStrolch to port Marlin 2.0.x, but with some new tweaks.

## Prerequisites

This configuration requires Marlin 2.1.1 (or bugfix-2.1.x after 25 June 2022). Marlin 2.1 works but you'll have to remove `LCD_CONTRAST_MIN`, `LCD_CONTRAST_MAX` and `LCD_CONTRAST_DEFAULT` from `Marlin/src/pins/ramps/pins_K8800.h`, otherwise the display will not work (appears blank).

This configuration requires a PlatformIO build environment.

To my knowledge, this is the first version of a configuration able to work with the mainstream unmodified Marlin core. This is thanks to the ongoing work of the Marlin team in improving the main firmware and the work of @SusisStrolch and @PsychoKiller1888, who correctly identified the most compatible display type and many other settings.

## Features

The firmware here is for the stock Velleman K8800, without any modifications. For the stock printer, it reproduces at least the functions of the original 1.1.4 firmware, with many issues removed. In particular:

- The calibration and bed leveling are more thorough and appear more accurate, although they are slower.
- There are far fewer head-to-bed crashes
- Providing that lubrication is adequate, belt slippage seems to be entirely eliminated.
- When using UBL, bed adhesion is far superior, even with the stock supplied BuildTak.

## WARNINGS

**NOTE: UBL REQUIRES CHANGES TO THE CURA CONFIGURATION (SEE BELOW)**

I use this configuration of the Marlin firmware now on an almost daily basis for both small and large prints, but you will no doubt encounter use cases I do not, and may therefore find bugs I have missed. The K8800 is particularly unforgiving of your supposed mistakes and I make no warranty of any kind that this firmware will work correctly for you. Start small and work up, use slower settings on Cura, especially for larger prints.

This firmware probes much closer to the outer edge than the stock firmware. **Be warned, you may need to increase sensitivity of the bed sensors using the knob at the back of the machine.** If during calibration or leveling, the nozzle starts to 'bump' the plate (i.e. actually move it up and down), to crash into the plate, or the probing fails, try increasing the sensitivity to maximum. If that still does not work, you likely have a faulty sensor, ask your supplier for replacements. The machine can get by on two working sensors with the normal firmware but not with this version. Be gentle with your sensors, they break easily.

Updates to firmware cannot fix underlying mechanical issues or user neglect. In particular:
- You **must** calibrate your printer fully before every print.
- You **must** recheck bed leveling during your print prologue (Cura does this by default).
- The bed must be correctly placed on the sensors, without any restriction of movement caused by the edges of the BuildTak or the moulding of the edge stops.

These are the result of design _"features";_ The cute circular Pyrex bed plate never goes back into the exactly the same position twice - so every print is different.

Also:
- The nozzle **must** be wiped at 120+ deg C temperature before each print - a tiny amount of residue on the end can easily throw the calibration and leveling off.
- You **must** clean and lubricate after every ten prints, or after a week of non-use. The supplied machine oil for the rails is pretty poor in my experience when compared to fine grade sewing machine oil, and you do need PTFE lubricant (not included) for the magnetic joints.

## Leveling Options

Choose bed leveling at the top of `Configuration.h` with either `K8800_UBL` or `K8800_BILINEAR`.

Bilinear Leveling uses the same approach as the original firmware, with the advantage of being able to work with the same K8800 profile shipped with Cura.

## Unified Bed Leveling and Cura

Unified Bed Leveling is more accurate due to the addition of manual probing, but requires changes to the Cura settings. **AT THIS TIME OF WRITING, THE AS-SHIPPED CURA PROFILE INCLUDES G-CODE COMMANDS THAT ARE INCOMPATIBLE WITH UBL AND IN ONE CASE MAY FORCE A HEAD CRASH DURING PREFLIGHT.**

Here is my amended version of the Start G-Code from Cura. To use this in Cura, go to:

*Preferences -> Configure Cura -> Printers -> Vertex Delta K8800 -> Machine Settings -> Start G-Code*

And paste in the following:

```
; Vertex Delta Start Gcode
M400
G28 ; Home extruder
M106 S128 ; Start fan
M104 T0 R50 ; Set cold nozzle
M109 T0 R50 ; Wait for cold nozzle
M117 Leveling bed...
G29 P1        ; Do automated probing of the bed.
G29 P3        ; Smart Fill Repeat until all mesh points are filled in, Used to fill unreachable points.
G29 S0        ; Save UBL mesh points to slot 0 (EEPROM).
G29 F 10.0    ; Set Fade Height for correction at 10.0 mm.
G29 A         ; Activate the UBL System.
M500          ; Save current setup. WARNING - UBL will be active at power up, before any G28.
G1 X0 Y100 Z1 F2000
; DO NOT USE G92 HERE - CONFLICTS WITH UBL
M107 ; Stop fan
G90 ; Absolute positioning
M82 ; Extruder in absolute mode
M104 T0 S{material_print_temperature}
G92 E0 ; Reset extruder position
M109 T0 S{material_print_temperature}
M117 Priming nozzle...
M83
G1 E20 F100 ; purge/prime nozzle
M82
G92 E0 ; Reset extruder position
G4 S3 ; Wait 3 seconds
G1 Z5 F2000
G1 Z5 X0 Y0
M117 Vertex Delta printing
```
