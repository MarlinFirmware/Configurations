# Ender 3 S1

## Flashing Mainboard Firmware

The bootloader which handles flashing new firmware on this board remembers the last filename you used.

Therefore, to flash the compiled firmware binary onto the board you must give the "`firmware.bin`" file on the SD card a unique name, different from the name of the previous firmware file, or you will be greeted with a blank screen on the next boot. This is done automatically if you compile using the Auto Marlin Build plugin in VSCode. Otherwise, rename the `*.bin` file accordingly.

Pay attention to the two versions of the motherboard for the S1, one is using a SoC STM32F1 and the other using a STM32F4:

 - Printers with factory firmware version **1.X.X** have the STM32F**1** SoC

 - Printers with factory firmware version **3.X.X** have the STM32F**4** SoC

 - You can also find out your version number by looking at the mainboard (its printed on the top of the SoC)

 - Installing 1.X.X stock firmware or a compiled one to the target STM32F**1** on STM32F**4** mainboards **might brick** them! And _vice-versa_.
    
Placing the firmware file into the SDCard:

 - STM32F1 mainboard, place the `*.bin` on the root folder

 - STM32F4 mainboard, place the `*.bin` on a folder named `STM32F4_UPDATE`
