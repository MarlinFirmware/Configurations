# Table of Contents <!-- omit in toc -->
- [# Back up your Working Printer Firmware](#back-up-your-working-printer-firmware)
  - [Save Printer Settings (Optional, but recommended)](#save-printer-settings-optional-but-recommended)
  - [Backup your Chitu Firmware (Optional, but strongly recommended)](#backup-your-chitu-firmare-optional-but-strongly-recommended)
- [Configuring Marlin for your Printer](#configuring-marlin-for-your-printer)
  - [1. Board Version](#1-board-version)
  - [2. Bed size](#2-bed-size)
  - [3. Stepper Drivers](#3-stepper-drivers)
  - [4. Steps / mm](#4-steps--mm)
  - [5. Other Marlin Config](#5-other-marlin-config)
- [Flashing Marlin JUST USING SD](#flashing-marlin-just-using-sd)
- [Flashing Marlin Firmware MANUALLY (OBSOLETE!)](#flashing-marlin-firmware-manually-obsolete)
- [Known Issues](#known-issues)
- [Suggested Printing Workflow](#suggested-printing-workflow)

# See X5SA readme
See the [X5SA readme](https://github.com/MarlinFirmware/Configurations/tree/import-2.1.x/config/examples/Tronxy/X5SA) for general information about this printer and its predecessor.

# Back up your Working Printer Firmware

## Save Printer Settings (Optional, but recommended)

You can (OR MUST) dump the current settings of your printer. It may help you to figure out some configs, like steps/mm of your extruder.

1. Create a file named `savesettings.gcode` with the following content:
```gcode
M6046 ; sdcard access
M8512 "currentconfig.gcode" ; save settings to file
```
2. Save it on the printer's SD card
3. Put the card in the printer and "print" this file
4. The printer won't do anything. Just wait a few seconds and stop the print.
5. Your current printer settings are stored in the file: `currentconfig.gcode`

You can read more about it in [this guide](https://www.facebook.com/notes/tronxy-turnigy-x5s-x5sa-x3s-3d-printer-drucker-users/tronxy-firmware-configuration-guide-by-keith-varin-addermk264bit-tuning/649799805579765/).

Thanks to KEITH VARIN.

## Backup your Chitu Firmare (Optional, but strongly recommended)

1. Turn off your printer
2. Open your board case
3. Remove the "boot" jumper (1) as the image.
4. Change the "v source" jumper (2) from 5V to USB.
5. Open [STM Cube Programmer](https://www.st.com/en/development-tools/stm32cubeprog.html) (linux, mac, windows) or [FLASHER-STM32](https://www.st.com/en/development-tools/flasher-stm32.html) (only windows)
6. The size must be **512kb -> 0x80000**
7. Save the file. It must have exactly 524288 bytes (512kb)
8. Disconnect
10. Unplug USB cable
11. Put back the "boot" jumper (1).
12. Put back the "v source" jumper to 5V.

![alt text](./chitu-board.jpg)


# Configuring Marlin for your Printer

You need to edit `Configuration.h` to set up your printer, and ensure platformio.ini is using the environment "chitu_f103".

## 1. Board Version

For ***V6***

```cpp
// For V6
#define MOTHERBOARD BOARD_CHITU3D_V6
```

## 2. Bed size

```cpp
// The size of the printable area
#define X_BED_SIZE 330
#define Y_BED_SIZE 330
...
#define Z_MAX_POS 400
```

## 3. Stepper Drivers

X5SA Pro models have TMC2225 drivers. Due to the code interface being the same as the TMC2208 drivers, Marlin has you use them. Currently UART mode is not known to work with the CXY-V6-191017 board, so the _STANDALONE version is used.

X5SA Pro (with TMC Drivers):

```cpp
/**
 * Stepper Drivers
 * ...
 */
#define X_DRIVER_TYPE TMC2208_STANDALONE
#define Y_DRIVER_TYPE TMC2208_STANDALONE
#define Z_DRIVER_TYPE TMC2208_STANDALONE
//#define X2_DRIVER_TYPE A4988
//#define Y2_DRIVER_TYPE A4988
//#define Z2_DRIVER_TYPE A4988
//#define Z3_DRIVER_TYPE A4988
//#define Z4_DRIVER_TYPE A4988
#define E0_DRIVER_TYPE TMC2208_STANDALONE
//#define E1_DRIVER_TYPE A4988
//#define E2_DRIVER_TYPE A4988
//#define E3_DRIVER_TYPE A4988
//#define E4_DRIVER_TYPE A4988
//#define E5_DRIVER_TYPE A4988
//#define E6_DRIVER_TYPE A4988
//#define E7_DRIVER_TYPE A4988
```

It has been observed that the default TMC2208 timings for the settings below are too fast, and can result in one or more of the stepper motors stopping in the middle of a print.

in configuration_adv.h
```cpp
#define MINIMUM_STEPPER_POST_DIR_DELAY 150
#define MINIMUM_STEPPER_PRE_DIR_DELAY 150
#define MINIMUM_STEPPER_PULSE_NS 150
```

## 4. Steps / mm

For the steps for X, Y and Z, one way to know the correct values is to read your `currentconfig.gcode` (saved earlier):

***! This part can vary from machine to machine !***

- `M8009` is the X and Y step/mm.
- `M8010` is the Z step/mm.
- `M8011` is the Extruder step/mm.

Example:

```gcode
M8009 S0.006250;x,y
M8010 S0.001250;z
M8011 S0.001308;e
```

Is equal to:

```gcode
x,y = 1 / 0.006250 = 160
z = 1 / 0.001250 = 800
e = 1 / 0.001308 = 764
```

Check your values!

So in Marlin for Titan PRO (tmc):
```cpp
#define DEFAULT_AXIS_STEPS_PER_UNIT   { 160, 160, 800, 764 }
#define INVERT_E0_DIR true // Extruder seems inverted on Titan due to geared extrusion!
```

## 5. Other Marlin Config

You can customize for your own setup. TFT, Baby Steps and a lot of cool stuff are already configured for you.

# Flashing Marlin JUST USING SD

Thanks to the amazing work of J.C. Nelson, now we can just use Marlin updating directly from SD!!

1. After you compile Marlin with the above instructions, it will generate a file: `YOUR-MARLIN-DIR/.pio/build/chitu_f103/update.cbd`
2. Turn off your printer
3. Copy the `update.cbd` file to SD card.
4. Put the SD card in your printer.
5. Power it on.
6. It will give some bips. After that, Marlin will start!

SIMPLE AS THAT!

Again, thanks to J.C. Nelson @xC000000

***If you already flashed Marlin the old way then you need restore your Chitu backup to use this method. This will make all your future installs easier.***

# Flashing Marlin Firmware MANUALLY (OBSOLETE!)

OBSOLETE! JUST USE THE FIRST METHOD.

1. Turn off the printer
2. Open the board case
3. Remove the "boot" jumper (1) as the image.
4. Change the V source jumper (2) from 5V to USB.
5. Open [STM Cube Programmer](https://www.st.com/en/development-tools/stm32cubeprog.html) (linux, mac, windows) or [FLASHER-STM32](https://www.st.com/en/development-tools/flasher-stm32.html) (only windows)
6. Flash the YOUR-MARLIN-DIR/.pio/build/chitu_f103/firmware.bin at 0x08000000
7. After the Flash is done, put the back the boot jumper (1) and the V source jumper to 5V.
8. Turn on the printer

![alt text](./chitu-board.jpg)

# Known Issues

Waiting on the pull request [28059](https://github.com/MarlinFirmware/Marlin/pull/28059) to allow configuration.h to have the override for the Z_STOP_PIN. As the CXY-V6-191017 board has this wired to PG9 instead of PA14 as other chitu_v6 boards do:

in configuration.h
```cpp
#define Z_STOP_PIN PG9
```

If this hasn't been merged yet, you'll need to edit the file Marlin/src/pins/stm32f1/pins_CHITU3D_V6.h

in Marlin/src/pins/stm32f1/pins_CHITU3D_V6.h replace:
```cpp
#define Z_STOP_PIN                          PA14
```

in Marlin/src/pins/stm32f1/pins_CHITU3D_V6.h with:
```cpp
#ifndef Z_STOP_PIN
  #define Z_STOP_PIN                          PA14
#endif
```

A patch may already have been applied to Marlin by the time you read this.

The maximum speeds have been left

# Suggested Printing Workflow

Due to the way the chitu firmware worked, and the inadiqicies of the print bed support structures, you'll likely need to change your normal workflow to be similar to below. Due to this workflow is why the bed leveling has been restricted to a 3x3 grid to save time during printing.

Initial changes
- change your slicer Machine start existing G-code to replace your existing G28 line with:
```text
G28 ; home all and clear ABL map
; Perform auto bed levelling and store in RAM for this print.
G29 P1
G29 A  F10.0 ; Activate UBL and set fade height to 10mm
; Do not bother saving the mesh as the bed support structure wobbles so much it is not helpful
```
- change your slizer Machine end G-code to have on its last line
```text
M22; Release SD card
```

Normal Workflow
1. Clean your print bed and power on.
2. If you haven't got the Z axis sync mod, sync your Z axis motors
3. Preheat your print bed and nozzle
4. Run the `Probe and Level -> Tramming Wizard`
  1. Using the tramming wizard menu starting from front-left press measure, wait for the probe to move and measure and for the measurement to come back as 0.0, then press done
  2. Continue to each of the other locations listed, however for each of the other locations, adjust the bed support screws until the bed is close enough to 0 for your liking. (normally adjust until they are between -0.05 and 0.05)
  3. Press done
5. From the `Probe and Level -> Z Probe Wizard` menu use a piece of paper to adjust the zero height.
6. From the `Configuration -> Store Settings` menu save these values to EEPROM. (You may need to confirm Z offset babysteps and save again)
7. Start your print. You may need to use the menu `Select from SD Card` rather than the SD card icon on the main screen as it doesn't always recognise there is an SD card in the machine.
8. As the print is laying down its first layer, monitor it to see if you need to adjust the Z offset. If so, use the ``Tune`` menu to adjust the Z offset while it's laying down its first layer.

