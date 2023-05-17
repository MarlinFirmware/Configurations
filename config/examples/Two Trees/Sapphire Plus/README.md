## Two Trees Sapphire Configurations

This folder contains two default configurations for the Two Trees Sapphire Plus V2. The V2 has Dual Z Axis limit switches, and the V2.1 has a single Z limit switch, as well as a different board.

## Supported Versions

|Version|Board|Z-axis switches|
|---|---|---|
| V2|MKS Robin Nano V1.2|2|
| V2.1| MKS Robin Nano V1.3|1|

Make sure you always test the endstops/limit switches after using this configuration, as newer printers may have slight electrical and mechanical differences.

#### Configuration differences on V2.1

- Build with BOARD_MKS_ROBIN_NANO_V1_3_F4;
- Disable ZMAX plug (Z increments lower the bed);
- Enable INVERT_Z_DIR (Z increments lower the bed);
- Disable PRINTCOUNTER (not supported with current settings);
- Rotate TFT 180º;
- Enable endstops always on;
- Disable multiple Z endstops;

## Available options

By default the standard Marlin Touch UI will be used. Enable the `SAPPHIRE_PLUS_MKS_UI` option for the MKS UI.

Enable the `SAPPHIRE_PLUS_BLTOUCH` option for BLTouch support.

Enable the `SAPPHIRE_PLUS_TMC_UART` option for TMC UART support for the X, Y and E steppers. Note: you will need some hardware modification skills to modify the stepper sticks. A solder pad needs to be bridged to connect PDN to USART pin. Then a 1K resistor and wire is needed to connect the USART pin to the appropriate spare pin on MKS Robin Nano V1.2 board.
