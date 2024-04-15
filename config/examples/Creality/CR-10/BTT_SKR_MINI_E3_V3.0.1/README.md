# CR10 v1 (12v) configuration for BTT's SKR MINI E3 V3.0(.1).

### All edited fields in configuration files can be found by searching for "// EDITED".

### IMPORTANT: You NEED to decide whether you want to use LIN_ADV or DIRECT_SUPPORT, so disable either one of them in Configuration_adv.h before attempting to build to not get an error.

If you have diag jumpers removed on X Y Z axis, meaning you are not using SENSORLESS_HOMING then go ahead and uncomment DIAG_JUMPERS_REMOVED in Configuration_adv.h.

# Major changes made compared to stock Configuration.h:

Drivers set to TMC2209;

Serial port settings;

Adjusted probing feedrates;

Added:
+ MPCTEMP;
+ S_CURVE_ACCELERATION;
+ BLTOUCH, using dedicated BLTOUCH port;
+ USE_PROBE_FOR_Z_HOMING;
+ Z_MIN_PROBE_REPEATABILITY_TEST;
+ FILAMENT_RUNOUT_SENSOR;
+ AUTO_BED_LEVELING_UBL;
+ LCD_BED_LEVELING;
+ Z_SAFE_HOMING;
+ SKEW_CORRECTION;
  
Removed:
- Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN;
- PIDTEMP(hotend);

# Major changes made compared to stock Configuration_adv.h:

Adjusted manual feedrates;

Adjusted TMC driver currents;

Configurable DIAG_JUMPERS_REMOVED;

Added:
+ HOTEND_IDLE_TIMEOUT;
+ USE_CONTROLLER_FAN;
+ BLTOUCH_HS_MODE;
+ ASSISTED_TRAMMING;
+ INPUT_SHAPING on X and Y;
+ ADAPTIVE_STEP_SMOOTHING;
+ LIN_ADVANCE;
+ ARC_SUPPORT;
+ DIRECT_STEPPING;
+ HYBRID_THRESHOLD;
+ EDGE_STEPPING;
+ MECHANICAL_GANTRY_CALIBRATION;

Removed:
- NO_WORKSPACE_OFFSETS;
