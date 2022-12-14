# BIQU B1 Firmware

In `Configuration.h` enable the `MOTHERBOARD BOARD_BTT_SKR_V1_4` option at the top to specify the BTT SKR V1.4 motherboard, otherwise the V2.0 board will be applied (slightly farther down).

For the SKR V2.0-based config, flash drive support is enabled by default. Jumpers to enable support may not have been installed correctly from the factory, so [follow Biqu's instructions, starting with Step 2](https://github.com/bigtreetech/BIQU-B1-SE-PLUS/blob/master/B1-SE%20fimware/B1-SE-U%20Disk%20Usage%20Tutorial-English.pdf) if flash drive support is not working correctly.

## BLTouch Probe Support

Uncomment `B1_USE_BLTOUCH` for probe customizations.

This configuration retains the use of homing with a Z limit switch. If you want to home with the BLTouch probe, remove your Z limit switch & bracket and enable (uncomment) `USE_PROBE_FOR_Z_HOMING` and `Z_SAFE_HOMING`. Change `Z_MIN_ENDSTOP_INVERTING` from `true` to `false`.
