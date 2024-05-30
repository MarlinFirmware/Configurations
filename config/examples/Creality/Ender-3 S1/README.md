# Ender 3 S1

## Flashing Mainboard Firmware

The bootloader which handles flashing new firmware on this board remembers the last filename you used.

Therefore, to flash the compiled firmware binary onto the board you must give the "`firmware.bin`" file on the SD card a unique name, different from the name of the previous firmware file, or you will be greeted with a blank screen on the next boot. The file rename is done for you when compiling with PlatformIO. Otherwise, rename the `*.bin` file accordingly.

Pay attention to the two versions of the motherboard for the S1, one is using a SoC STM32F1 and the other using a STM32F4:

 - Ender 3 printers that come with a firmware version **1.x.x** have the **STM32F1** chip.
 - Ender 3 printers that come with a firmware version **3.x.x** have the **STM32F4** chip.
 - Check the version number on the STM32Fx chip itself to confirm you have the correct version.
 - Installing 1.x.x stock firmware or a compiled one to the target **STM32F1** on **STM32F4** mainboards **might brick** them! And _vice-versa_.

Where to put the firmware file on the SDCard:

 - STM32F1 board: Put the `*.bin` file into the root folder.
 - STM32F4 board: Put the `*.bin` file into a folder named `STM32F4_UPDATE`.
