# Ender-5 Plus Configurations for Marlin Firmware

## Important

NOTE: The factory LCD firmware is only compatible with Creality firmware. The LCD standard UI will not function. This is expected.

## Marlin DGUS UI Instructions

The factory LCD can use the Marlin DGUS interface, available at https://github.com/coldtobi/Marlin_DGUS_Resources. This is optional. But without it Marlin will only work through an external client attached via USB.

Flash the LCD with a microSD card inserted into the slot on the LCD panel inside the printer (not the main SD slot). The front panel must be disassembled for access. The microSD card must be <= 8 GB and formatted with a 4K cluster size. Copy the DWIN_SET folder to the microSD card. Insert it into the LCD while powered off, then power on the printer. You should see a blue status screen, the LCD cycle through the UI background interfaces, then stop with a "SD Card Process... END!" message. Afterwards, remove the microSD card and power cycle the printer again.

The Creality firmware can be restored by downloading the Ender 5 Plus firmware from https://www.creality.com/download and following the above flashing procedure with the Creality-provided DWIN_SET folder.

NOTE: you may need to physically rotate the LCD 180˚ before reinstalling into the printer for the UI to be the right side up.

## Marlin DGUS UI Limitations

The Information button (letter i in a circle) does not function at this time.
Tools menu does not do anything at this time.
If you press the tools menu icon and then enter another menu then go back you will end up at the boot screen again with no apparent way out. You can just press anywhere on this screen and it will return to the status screen.

