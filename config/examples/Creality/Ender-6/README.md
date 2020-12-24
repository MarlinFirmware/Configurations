# Ender-6 Configurations for Marlin Firmware

## Install USB Console Cable Before Starting

The Ender 6 does not ship with an accessible USB port. It is a good idea to open the bottom panel on the printer base and connect a USB cable to the micro-USB port on the motherboard. Even if the factory LCD is reflashed with compatible firmware, not all features will be accessible. A USB console cable will allow the printer to be controlled without the LCD and provide full functionality.

## BLTouch Instructions

There are two Configuration.h options. One contains values for factory installed or retrofitted BLTouch sensors. While Creality is not shipping printers with this option at this time, the existence of factory mounts, wiring, and OEM firmware supporting it suggests this may change in the future. Select the file appropriate for your setup.

NOTE: Due to slight manufacturing differences, each user should tune the BLTouch z-offset for their specific printer.

## Flashing Instructions

Copy the compiled "firmware.bin" file to an SD card. Insert it into the printer while powered off, then power it on. The procedure will take a few seconds.

The printer remembers the name of the last used firmware file. Every new firmware file name must be different from the previously used file name.

NOTE: The factory LCD firmware is only compatible with Creality firmware. The LCD will not show the progress bar increment and the standard UI will not function. This is expected.

## Marlin DGUS UI Instructions

The factory LCD can use the Marlin DGUS interface available at https://github.com/coldtobi/Marlin_DGUS_Resources. This is optional. Marlin will still work through an external client attached via USB (see first section).

Flash the LCD with a microSD card inserted into the slot on the LCD panel inside the printer (not the main SD slot). The front panel must be disassembled for access. The microSD card must be <= 8 GB and formatted with a 4K cluster size. Copy the DWIN_SET folder to the microSD card. Insert it into the LCD while powered off, then power on the printer. You should see a blue status screen, the LCD cycle through the UI background interfaces, then stop with a "SD Card Process... END!" message. Afterward, remove the microSD card and power cycle the printer again.

The Creality firmware can be restored by downloading the Ender 6 V1.0.1 firmware from https://www.creality.com/download and following the above flashing procedure with the Creality-provided DWIN_SET folder.

NOTE: you may need to physically rotate the LCD 180˚ before reinstalling into the printer for the UI to be the right side up.
