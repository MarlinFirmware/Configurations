# BIQU B1 (SKR 1.4) Firmware

Compile with the `LPC1768` environment.

## BLTouch Probe Support

Uncomment `B1_USE_BLTOUCH` for probe customizations.

This configuration retains the use of homing with a Z limit switch. If you want to home with the BLTouch probe, remove your Z limit switch & bracket and enable (uncomment) `USE_PROBE_FOR_Z_HOMING` and `Z_SAFE_HOMING`. Change `Z_MIN_ENDSTOP_INVERTING` from `true` to `false`.
