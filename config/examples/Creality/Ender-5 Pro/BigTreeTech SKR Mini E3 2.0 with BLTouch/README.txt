The configuration was made on a Phaetus Dragon hotend and a BMG clone extruder,
running the Leon-Me Gen 5 cooling shroud with dual 5015s.

Changes:

Configuration.h:
Defined SERIAL_PORT to 2
Defined SERIAL_PORT_2 to -1
Defined MOTHERBOARD to BOARD_BTT_SKR_MINI_E3_V2_0
Defined PIDTEMPBED and set default values
Defined EXTRUDE_MAXLENGTH to 600 to allow BMG extruder load/unload
Defined {X,Y,Z,E}_DRIVER_TYPE to TMC2209
Defined CLASSIC_JERK and set default values
Undefined Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN
Defined USE_PROBE_FOR_Z_HOMING
Defined Z_MIN_PROBE_PIN to PC14
Defined BLTOUCH
Defined PROBING_MARGIN to 8
Defined XY_PROBE_FEEDRATE and Z_PROBE_FEEDRATE_FAST to faster values
Defined MULTIPLE_PROBING to 2
Defined INVERT_{X,Y,Z,E0}_DIR to true
Defined X_BED_SIZE to 230 to regain bed size
Defined Y_BED_SIZE to 225 to regain bed size
Defined SOFT_ENDSTOPS_MENU_ITEM
Defined AUTO_BED_LEVELING_BILINEAR
Defined RESTORE_LEVELING_AFTER_G28
Defined PREHEAT_BEFORE_LEVELING and set default values
Defined G26_MESH_VALIDATION
Defined GRID_MAX_POINTS_X to 9
Defined EXTRAPOLATE_BEYOND_GRID
Defined MESH_EDIT_GFX_OVERLAY, MESH_INSET to 10 and GRID_MAX_POINTS_X to 9 in case user wants to use UBL
Defined LCD_BED_LEVELING
Defined MESH_EDIT_MENU
Defined LEVEL_BED_CORNERS
Defined Z_SAFE_HOMING
Defined HOMING_FEEDRATE_MM_M with faster values
Defined NOZZLE_PARK_FEATURE
Undefined SPEAKER to fix fan stuck at 100% bug
Defined FAN_SOFT_PWM for my dual 5015 setup

Configuration_adv.h:
Defined USE_CONTROLLER_FAN
Defined CONTROLLER_FAN_EDITABLE
Defined BLTOUCH_DELAY to 500
Defined PROBE_OFFSET_WIZARD
Defined BROWSE_MEDIA_ON_INSERT
Defined LONG_FILENAME_HOST_SUPPORT
Defined SDCARD_CONNECTION to ONBOARD
Defined BABYSTEP_ZPROBE_OFFSET and BABYSTEP_ZPROBE_GFX_OVERLAY
Defined LIN_ADVANCE and set default value
Defined ARC_P_CIRCLES
Defined ADVANCED_PAUSE_FEATURE
Defined FILAMENT_CHANGE_UNLOAD_LENGTH to 500
Defined ADVANCED_PAUSE_CONTINUOUS_PURGE
Defined ADVANCED_PAUSE_PURGE_LENGTH to 600
Defined PARK_HEAD_ON_PAUSE
Defined all SLAVE_ADDRESS to SKR values
Defined {X,Y}_STALL_SENSITIVITY to 50
Defined IMPROVE_HOMING_RELIABILITY