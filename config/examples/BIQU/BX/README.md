# BIQU BX Configuration

In `Configuration.h` enable the `MOTHERBOARD BOARD_BTT_SKR_SE_BX_V3` option at the top to specify the BTT SKR SE BX V3.0 motherboard, otherwise the V2.0 board will be applied (slightly farther down).

Enable the `BX_ALL_METAL_HOTEND` option to permit higher printing temperatures for the newer H2 extruder with an all-metal heatbreak.

Enable the `BX_SWAP_ZM_E1M` option to swap Z and E1 motors if they swapped from the factory. This will fix potential issues with [`G34 - Z Steppers Auto-Alignment`](https://marlinfw.org/docs/gcode/G034-zsaa.html) not working correctly.

## Homing with a Probe

This configuration retains the use of homing with a Z limit switch. If you If you want to home with the inductive probe, remove your Z limit switch & bracket and enable (uncomment) `USE_PROBE_FOR_Z_HOMING` and `Z_SAFE_HOMING`.
