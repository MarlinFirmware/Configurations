# Creality Ender-5 S1 — Touch Screen

This configuration drives the stock resistive touch screen (`CREALITY_RTS`). To use the Creality / CR-10 12864 knob display on the board's "LCD" header instead, see the [CR10 Stock Display](../CR10%20Stock%20Display) configuration.

## (Work in progress, waiting on https://github.com/MarlinFirmware/Marlin/pull/25382 to support the screen) 

The bootloader on the stock board has special requirements and requires a flag to be set in the EEPROM before it will install the firmware.

- The built firmware bin file must be placed into a folder named `STM32F4_UPDATE` on the SD card.
- Connect to the printer over serial and send `M936 V2`. (You can also run a G-code file containing `M936 V2`.)
- Make sure to always flash a working version of Marlin with `OTA_FIRMWARE_UPDATE` enabled!
- If for any reason you can't run `M936 V2` then you'll need to run a sketch to write 0x01 to EEPROM address 90 (e.g., with `BL24CXX::write`). (A value of 0x02 selects the screen update instead; that is what `M936 V3` sets.)

## Fixed-Time Motion

[Fixed-Time Motion](https://marlinfw.org/docs/features/ft_motion.html) (FT Motion) is an alternative motion system that plans moves on a fixed time step and can apply input shapers to reduce ringing. It is compiled in here but off at startup, so the printer uses standard motion until you switch it on:

- `M493 S1` turns FT Motion on and `M493 S0` turns it off (see [M493](https://marlinfw.org/docs/gcode/M493.html)).
- The shapers start as `NONE` and no frequencies are tuned. Find your printer's frequency with the methods on the [Input Shaping](https://marlinfw.org/docs/features/input_shaping.html) page, set it with `M493`, and save with `M500`.
- FT Motion is new, so test it with a few small prints first.
