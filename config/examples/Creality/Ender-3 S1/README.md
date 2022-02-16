# Ender 3 S1

# Ender 3 V2

## Flashing Firmware

The bootloader which handles flashing new firmware on this board remembers the last filename you used.

Therefore, to flash the compiled firmware binary onto the board you must give the "`firmware.bin`" file on the SD card a unique name, different from the name of the previous firmware file, or you will be greeted with a blank screen on the next boot.

## Updating the Display

Currently there is no Marlin-specific firmware available, so flash the latest official firmware to the display. There are some minor graphical glitches but the display is very usable.

Download the latest Ender 3 S1 firmware [from www.creality.com/download](https://www.creality.com/download) and flash as follows:

- Copy the `private` folder to a 4096k formatted FAT32 microSD card and insert the card into the slot on the back of the display unit.
- Power on the machine and wait for the screen to show a filled progress bar and show "Update finished!". The display will reset shortly after displaying this message.
- Power off the machine.
- Remove the SD card from the back of the display.
- Power on to confirm a successful flash.
