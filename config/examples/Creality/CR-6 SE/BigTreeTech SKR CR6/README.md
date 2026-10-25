Creality CR-6 SE with a BigTreeTech SKR CR6 board and the stock touch screen.

- Requires the CR-6 Community touch-screen firmware v61 or newer on the screen.
- Build with the `STM32F103RE_btt` environment. If you build with `STM32F103RE_btt_USB` the SD card is also shared with the computer as a USB drive, which can freeze the printer when the file list is opened while a host is connected. In that case enable `NO_SD_HOST_DRIVE`.
- Some printers need `ENDSTOP_NOISE_THRESHOLD 2` for reliable probing. It is commented out here.
- `EEPROM_AUTOSAVE_AFTER` saves settings edited on the screen a few seconds later. Comment it out to save only with `M500`.
