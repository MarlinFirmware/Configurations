# Ender 3 Pro V1.5

This is a surprise upgrade to the Ender 3 Pro that some customers seem to have started receiving in mid July 2020 time frame.
There seems to be no documentation about it nor is there any support page for it. 
It appears to be an Ender 3 V2 board placed in an Ender 3 Pro body along with the stock Ender 3 Pro display.
Best way to confirm you have this is to look at the control board and confirm it has a PCB v4.2.2 on it.

Please set default_envs = STM32F103RET6_creality in file platformio.ini in Marlin root folder.

This config is derrived from the Ender 3 V2 config and support for CR-10 display is enabled (since that is the display it the product seems to be shipping with).

## Flashing Firmware

The bootloader which handles flashing new firmware on this board remembers the last filename you used.

Therefore, to flash the compiled firmware binary onto the board you must give the "`firmware.bin`" file on the SD card a unique name, different from the name of the previous firmware file, or you will be greeted with a blank screen on the next boot.
