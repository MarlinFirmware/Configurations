Creality CR-6 SE with a BigTreeTech SKR CR6 board and the stock touch screen.

- Requires the CR-6 Community touch-screen firmware v61 or newer on the screen.
- Build with the `STM32F103RE_btt` environment. The `STM32F103RE_btt_USB` environment also shares the SD card with the computer as a USB drive. One tester reported USB problems and freezes with that environment, and the shared SD card is the suspected cause (not confirmed). If you need that environment, try enabling `NO_SD_HOST_DRIVE`.
- Some printers need `ENDSTOP_NOISE_THRESHOLD 2` for reliable probing. It is commented out here.
- `EEPROM_AUTOSAVE_AFTER` saves settings edited on the screen a few seconds later. Comment it out to save only with `M500`.
- `LEVELING_HEAT_SOAK_TIME 300` makes the Z Offset screen's Home and automatic leveling heat the bed and nozzle to the Leveling Settings temperatures and wait 5 minutes first, since the bed and nozzle change shape and size as they warm up. If the bed is already at temperature there is no wait. Lower or comment it out if you prefer.
