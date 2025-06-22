# Space Issues
## Version Differences
The single extruder build fits more than the dual such as `S_CURVE_ACCELERATION`. 2.1.3 is slightly bigger than 2.1.2.5 which affects fitting `HOTEND_IDLE_TIMEOUT`, on 2.1.3 Dual Extruder builds you can disable `CAPABILITIES_REPORT` to fit this. I didn't do it in the example to prevent minor future changes to the firmware from causing the build to be too large. `CONFIGURE_FILAMENT_CHANGE` which did not exist on 2.1.2 is disabled in the dual build to fit the filament loading menu.

## Features disabled/enabled to save space.
```
AUTOTEMP
SDCARD_READONLY
NO_SD_AUTOSTART
ARC_SUPPORT
NO_VOLUMETRICS
NO_WORKSPACE_OFFSETS
```

# Flashing
## USB Flashing
MakerBot's Mightyboard Rev E’s are missing capacitor c20. This prevents the board from self resetting to flash over USB. You can try to time pressing the reset button with uploading firmware. I have only ever accomplished this once.

## ICSP Flashing
I find it much easier to flash over the ICSP header using an Arduino and AVR Dude. Adjust settings as necessary such as the port or if you are using a different device to flash. Feel free to reach out to the author of this config in Discord for help.\
`avrdude -v -patmega1280 -cstk500v1 -PCOM4 -b19200 -U flash:w:firmware.hex`

# Printer Information
## Primary Extruder (Dual)
The right nozzle is Extruder 1 (E0) on this printer which will often be confusing as it will be the left temperature on the screen. There are a couple of ways to change this, you can pin swap the pins file. Don’t forget to invert the motor direction. It is possible but not as easy to edit the display order instead.

## Motor Current
The FlashForge Creator Pro example sets current a little higher at .84 for most and .4 for Z. I have matched the MakerBot values from beta.ivc.no of .81 except for Z rounding from .278 to .28. The Z motor will whine way more at higher current.

# Modifications

## Part Cooling Fan
If you have added a part cooling fan to the extra mosfet you need to uncomment #define NUM_M106_FANS\
`#define NUM_M106_FANS 1`

You will also need to set the pin definition. This can actually be inserted right below the line you just uncommented.\
`#define FAN0_PIN                  MOSFET_F_PIN`

