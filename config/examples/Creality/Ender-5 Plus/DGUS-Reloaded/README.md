# Ender-5 Plus Configurations for Marlin Firmware

## Marlin DGUS UI "Reloaded" Instructions

To use `DGUS_LCD_UI RELOADED` the stock LCD must be flashed with custom firmware.

### Get the DWIN_SET

- Download the [bundled `DWIN_SET` archive](DWIN_SET.tar.gz) from the same Configurations branch as these files.
- Use it with the matching Marlin version. Display files from another version may be incompatible (for example, temperatures may display at one tenth of their actual value).
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
- When the procedure ends the screen will display a blue background with an END message on the first line and a summary.
- Turn off the printer. Remove the Micro-SD card from the touchscreen. Reassemble the printer if needed.
- The touch-screen firmware is now up-to-date.
