# Ender-5 Plus with BTT SKR 3 Configurations for Marlin Firmware

## Important

The LCD will need the cable modified to fit the SKR 3 motherboard.
Four pins, tx2-pa10 rx2-pa9 gnd-g 5v-+5v, ( See the boards silkscreens for pin labels)

## About

These are configuration files for the Ender 5 Plus to work with a BTT SKR 3 motherboard using the stock LCD with A4988 stepper drivers.

## Marlin DGUS UI "Reloaded" Instructions

To use `DGUS_LCD_UI RELOADED` the stock LCD must be flashed with custom firmware.

### Get the DWIN_SET

- Download the `DWIN_SET` archive from https://github.com/MarlinFirmware/Configurations/raw/bugfix-2.1.x/config/examples/Creality/Ender-5%20Plus/DGUS-Reloaded/DWIN_SET.tar.gz
- Extract the contents of the archive. You should now have a folder called `DWIN_SET`.

### Prepare the SD Card

- Format a Micro-SD card, selecting FAT32 for the file system and 4096 bytes sector size. These parameters are required for the procedure to work.
- Copy the `DWIN_SET` folder to the root of the Micro-SD card.
- Unmount and unplug your Micro-SD card.

### Flash the touchscreen

- Turn off and unplug your printer (both power and USB).
- You will need to access the Micro-SD slot on the back of the touchscreen (not the one that may be on your mainboard). If necessary, open the printer to access this slot.
- Insert the Micro-SD card into the screen SD slot.
- Plug the printer's power cable back in (but not the USB cable) and turn on the printer.
- After a few seconds the screen background will turn blue and the firmware flash will begin. _Do not cut power to the printer while the procedure is running!_
- When the procedure ends the screen will display a blue background with an END message and summary.
- Turn off the printer. Remove the Micro-SD card from the touchscreen. Reassemble the printer if needed.
- The touch-screen firmware is now up-to-date.
