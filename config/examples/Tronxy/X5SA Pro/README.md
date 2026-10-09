# Table of Contents

- [Back Up Your Working Printer Firmware](#back-up-your-working-printer-firmware)
  - [Save Printer Settings (Optional, but Recommended)](#save-printer-settings-optional-but-recommended)
  - [Backup Your Chitu Firmware (Optional, but Strongly Recommended)](#backup-your-chitu-firmware-optional-but-strongly-recommended)
- [Configure Marlin for Your Printer](#configure-marlin-for-your-printer)
  - [1. Board Version](#1-board-version)
  - [2. Bed Size](#2-bed-size)
  - [3. Stepper Drivers](#3-stepper-drivers)
  - [4. Steps / mm](#4-steps--mm)
  - [5. Other Marlin Config](#5-other-marlin-config)
- [Flash Marlin Using SD Card](#flash-marlin-using-sd-card)
- [Flash Marlin Manually (Obsolete)](#flash-marlin-manually-obsolete)
- [Known Issues](#known-issues)
- [Suggested Printing Workflow](#suggested-printing-workflow)

---

## See X5SA Readme

For general information about the X5SA printer and its predecessor, see the
[X5SA Readme on GitHub](//github.com/MarlinFirmware/Configurations/tree/import-2.1.x/config/examples/Tronxy/X5SA).

---

## Back Up Your Working Printer Firmware

# Save Printer Settings (Optional, but recommended)

You can (OR MUST) dump the current settings of your printer. It may help you to figure out some configs, like steps/mm of your extruder.

1. Send `M503` to see a report of the current settings in your host.
2. Create a file named `savesettings.gcode` with the following contents:
```gcode
M6046 ; sdcard access
M8512 "currentconfig.gcode" ; save settings to file
```
3. Save it on the printer's SD card
4. Put the card in the printer and "print" this file
5. The printer won't do anything. Just wait a few seconds and stop the print.
6. Your current printer settings are stored in the file: `currentconfig.gcode`

You can read more about it in [this guide](//www.facebook.com/notes/tronxy-turnigy-x5s-x5sa-x3s-3d-printer-drucker-users/tronxy-firmware-configuration-guide-by-keith-varin-addermk264bit-tuning/649799805579765/).

Thanks to KEITH VARIN.

### Backup Your Chitu Firmware (Optional, but Strongly Recommended)

1. Turn off the printer.
2. Open the board case.
3. Remove the “boot” jumper (1) as shown in the image.
4. Switch the “V source” jumper (2) from 5V to USB.
5. Open **STM Cube Programmer** (Linux, macOS, Windows) or **FLASHER‑STM32** (Windows only).
6. The firmware image must be **512KB (0x80000)**. The file must be exactly 524,288 bytes.
7. Save the image.
8. Disconnect the USB cable.
9. Re‑install the “boot” jumper (1).
10. Re‑install the “V source” jumper to 5V.

---

## Configure Marlin for Your Printer

Edit `Configuration.h` and ensure that `platformio.ini` uses the `chitu_f103` environment.

### 1. Board Version

For the V6 board:

```cpp
#define MOTHERBOARD BOARD_CHITU3D_V6
```

### 2. Bed Size

```cpp
#define X_BED_SIZE 330
#define Y_BED_SIZE 330
#define Z_MAX_POS 400
```

### 3. Stepper Drivers

The X5SA Pro models use TMC2225 drivers. Marlin treats them like TMC2208 drivers, so use the “stand‑alone” mode. UART mode is not yet supported on the CXY‑V6‑191017 board.

```cpp
#define X_DRIVER_TYPE TMC2208_STANDALONE
#define Y_DRIVER_TYPE TMC2208_STANDALONE
#define Z_DRIVER_TYPE TMC2208_STANDALONE
#define E0_DRIVER_TYPE TMC2208_STANDALONE
```

The default TMC2208 timing values are too fast for many machines, so adjust them in `Configuration_adv.h`:

```cpp
#define MINIMUM_STEPPER_POST_DIR_DELAY 150
#define MINIMUM_STEPPER_PRE_DIR_DELAY 150
#define MINIMUM_STEPPER_PULSE_NS 150
```

### 4. Steps / mm

Read your `currentconfig.gcode` to determine the correct values:

- `M8009` → X/Y steps/mm
- `M8010` → Z steps/mm
- `M8011` → Extruder steps/mm

Example output:

```gcode
M8009 S0.006250 ; x,y
M8010 S0.001250 ; z
M8011 S0.001308 ; e
```

Convert to steps per unit:

```
x,y = 1 / 0.006250 = 160
z   = 1 / 0.001250 = 800
e   = 1 / 0.001308 = 764
```

So in Marlin (Titan PRO with TMC drivers) you'd set:

```cpp
#define DEFAULT_AXIS_STEPS_PER_UNIT { 160, 160, 800, 764 }
#define INVERT_E0_DIR true   // Extruder appears inverted on Titan due to geared extrusion
```

### 5. Other Marlin Config

The README already includes ready‑to‑use settings for TFT, Baby‑Steps, and other advanced features. Feel free to tweak them for your own setup.

---

## Flash Marlin Using SD Card

Thanks to the excellent work of J.C. Nelson, you can now update Marlin directly from an SD card.

1. Compile Marlin with the settings above. The build output will be `YOUR-MARLIN-DIR/.pio/build/chitu_f103/update.cbd`.
2. Power off the printer.
3. Copy `update.cbd` to an SD card and insert it.
4. Turn the printer on. You'll hear a series of beeps, then Marlin will begin the update.

That's all—no need to open the case or use a programmer.

If you previously flashed Marlin the old way, restore your Chitu backup before using this method; it will simplify future updates.

---

## Flash Marlin Manually (Obsolete)

This method is no longer recommended. If you must use it:

1. Power off the printer.
2. Open the board case.
3. Remove the “boot” jumper (1).
4. Change the “V source” jumper (2) from 5V to USB.
5. Open **STM Cube Programmer** or **FLASHER‑STM32**.
6. Flash `YOUR-MARLIN-DIR/.pio/build/chitu_f103/firmware.bin` to address `0x08000000`.
7. Re‑install the “boot” jumper (1) and return the “V source” jumper to 5V.
8. Power on the printer.

---

## Known Issues

The pull request [28059](//github.com/MarlinFirmware/Marlin/pull/28059) has not yet merged. Until it does, you must manually override the Z‑stop pin in `pins_CHITU3D_V6.h` because the CXY‑V6‑191017 board uses PG9 instead of PA14.

In `pins_CHITU3D_V6.h` replace:

```cpp
#define Z_STOP_PIN PA14
```

with:

```cpp
#ifndef Z_STOP_PIN
  #define Z_STOP_PIN PA14
#endif
```

---

## Suggested Printing Workflow

Because the Chitu firmware behaves differently and the bed support structure can wobble, it's best to follow this workflow. The UBL mesh is limited to a 3×3 grid to save time.

### Initial Changes

1. Replace your slicer's machine‑start G‑code with:

   ```text
   G28 ; home all axes and clear ABL map
   G29 P1
   G29 A F10.0 ; activate UBL and set fade height to 10mm
   ```

   (Do not save the mesh; the support structure's wobble makes it unreliable.)

2. End‑print G‑code: add `M22` (Release SD card) on the last line.

### Normal Workflow

1. Clean the print bed and power on the printer.
2. If you haven't installed the Z‑axis sync modification, do it now.
3. Preheat the bed and nozzle.
4. Run “Probe and Level → Tramming Wizard” from the menu:
   - Measure the front‑left corner and confirm a 0.0 reading.
   - Repeat for the remaining corners, adjusting the bed screws until the readings are within –0.05mm to +0.05mm.
5. Use “Probe and Level → Z Probe Wizard” to set the zero height with a sheet of paper.
6. Save the values to EEPROM with “Configuration → Store Settings.” (You may need to confirm the Z‑offset babysteps and save again.)
7. Start the print. If the first layer looks uneven, use babystepping to adjust the Z position. The `BABYSTEP_Z_PROBE` command also updates the probe offset for future leveling. Save the adjustment with `M500`.

Enjoy a smoother printing experience!
