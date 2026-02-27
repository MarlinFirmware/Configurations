# Creality Ender-5 S1

The bootloader on the stock board has special requirements and requires a flag to be set in the EEPROM before it will install the firmware.

- The built firmware bin file must be placed into a folder named `STM32F4_UPDATE` on the SD card.
- Connect to the printer over serial and send `M936 V2`. (You can also run a G-code file containing `M936 V2`.)
- Make sure to always flash a working version of Marlin with `OTA_FIRMWARE_UPDATE` enabled!
- If for any reason you can't run `M936 V2` then you'll need to run a sketch to write 0x02 to EEPROM address 90 (e.g., with `BL24CXX::write`).
