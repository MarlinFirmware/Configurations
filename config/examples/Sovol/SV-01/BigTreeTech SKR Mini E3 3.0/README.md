## SKR Mini E3 V3 Board

These files configure Marlin for a Sovol SV01 with `MOTHERBOARD BOARD_BTT_SKR_MINI_E3_V3_0` board installed with silent stepper drivers and a Fixed Probe.
The probe is configured to use the Z endstop port on the board.

### Probe and Offsets

- Enable the `SOVOL_FIXED_PROBE` option for a `FIXED_MOUNTED_PROBE`.
- You'll need to to adjust the `NOZZLE_TO_PROBE_OFFSET` values according to your probe's mounting location.
