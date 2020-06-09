
# Configuring your board

In the Configuration.h you can change board to V5, V6, and so on.

You can make your on setup.

# Flashing the new firmware

1. Turn off your printer
2. Open your board case
3. Remove the "boot" jumper (1) as the image.
4. Change the v source jumper (2) from 5V to USB.
5. Open [STM Cube Programmer](https://www.st.com/en/development-tools/stm32cubeprog.html) (linux, mac, windows) or [FLASHER-STM32](https://www.st.com/en/development-tools/flasher-stm32.html) (only windows)
6. Flash the YOUR-MARLIN-DIR/.pio/build/chitu_f103/firmware.bin at 0x08000000 
7. After the flash finished, put the back the boot jumper (1) and the v source jumper to 5V.
8. Turn On your Printer!

