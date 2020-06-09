# Befort start (Optional, but recommended)

You can dump the current settings of your printer. It may help you to figure out some configs, like steps/mm of your extruder.

1. Create a file named ``savesettings.gcode`` with the followig content:
```
M6046 ;sdcard access
M8512 "currentconfig.gcode" ;save settings to file
```
2. Save it in your printer SD
3. Put it on your printer and "print" this file
4. The printer won't do anything, just wait a few seconds and stop the print.
5. Your current printer settings are stored in the file: ``currentconfig.gcode``

You can read more about in: https://www.facebook.com/notes/tronxy-turnigy-x5s-x5sa-x3s-3d-printer-drucker-users/tronxy-firmware-configuration-guide-by-keith-varin-addermk264bit-tuning/649799805579765/

Thanks to KEITH VARIN.

# Configuring your board

In the Configuration.h you can change board to V5, V6, and so on.

You can make your on setup.

TFT, Baby Steps and a lot of cool stuff are already configured for you!

# Flashing the new firmware

1. Turn off your printer
2. Open your board case
3. Remove the "boot" jumper (1) as the image.
4. Change the v source jumper (2) from 5V to USB.
5. Open [STM Cube Programmer](https://www.st.com/en/development-tools/stm32cubeprog.html) (linux, mac, windows) or [FLASHER-STM32](https://www.st.com/en/development-tools/flasher-stm32.html) (only windows)
6. **BACKUP** your current firmware
7. Flash the YOUR-MARLIN-DIR/.pio/build/chitu_f103/firmware.bin at 0x08000000 
8. After the flash finished, put the back the boot jumper (1) and the v source jumper to 5V.
9. Turn On your Printer!

