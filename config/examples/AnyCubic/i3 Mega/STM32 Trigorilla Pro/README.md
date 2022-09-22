# Marlin Configs for the 32 Bit Motherboard Variant of the I3 Mega
(STM32F1 Trigorilla Pro)

## Using the Configs
Load them into Marlin like any other configs. Set `default_envs = trigorilla_pro` in `platformio.ini` to build successfully. Flashing through PlatformIO seems to be broken, you can use stm32flash to flash with `stm32flash -w firmware.bin -v -g 0x0 -b 115200 <YOUR COM/SERIAL PORT HERE>` in the terminal. Octoprint firmware flasher plugin works too. <br>
You need to remover Jumper JP1 on the board to access the bootloader and flash firmware. You can also set SW1 to USB to power the STM32 solely through USB, otherwise the PSU needs to be on to flash. If you need to flash often it may be worth soldering a button that has a normally closed pin to a BEC plug, and plug that into JP1 instead of the Jumper. That switch can be routed to the outside of the case and held down at boot to enable flashing mode.

## Features
- Full working touch screen with Marlin touch menu
- Model predictive temperature control for stable hotend temperatures (tune with M306 T)
- PID hotend baseline tune included as well
- PID bed heating
- SD Card works
- Filament runout sensor
- Babystepping for realtime first layer adjustments
- Pre-Tuned linear advance (high at 0.8, reduce to 0.6 if you see underextrusion)
- Manual bed levelling (UBL)
- Power loss recovery
- Support for BLTOUCH (derrived from AVR I3 Mega configs, untested)
- Support for TMC2208 (derrived from AVR I3 Mega configs, untested)

## Potential Issues
The Trigorilla Pro board has a large amount of issues and weird things. Even Anycubic likes to pretend it doesn't exist (They do not offer firmware for it on their website). 

Among the list of issues are:
- Unstable Vref causes very noisy (+-6°C) temperature measurements on the extruder.
- This can be exacerbated by plugging in a SD Card
- Power Supply has drops in voltage on bed heating start/stop, causing Vref to jump and temperature measurements to deviate. 
- Ground Loop with the case severely increases Vref noise

Fixes:
- Print or use plastic bolts and washers to isolate the board from the case. (https://www.printables.com/model/188956-m3-nuts-washer-and-bolts)
- Print over Serial not SD Card

## Credits
This project would not have been possible without the Marlin Discord and their many helpful members. I would like to thank especially The-EG, EvilGremlin, tombrazier, Dust and Nuck-TH. Additionally [this](https://www.thingiverse.com/thing:5159397/comments) unfinished firmware from Thiniverse user Thr333DDD is what I used to base these configs on. [This](https://github.com/napyk/trigorilla-pro) analysis and reverse engineering of the Trigorilla Pro board by Github user napyk was also very helpful in figuring out issues.

## Full List of Changes
```
---------------IN CONFIGURATION.H---------------

//#define I3MEGA_HAS_BLTOUCH //untested
//#define I3MEGA_HAS_TMC2208 //untested

#define MOTHERBOARD BOARD_TRIGORILLA_PRO

#define SERIAL_PORT 1

#define CUSTOM_MACHINE_NAME "I3 Mega"


#if ENABLED(I3MEGA_HAS_TMC2208)
  #define ALL_DRIVERS_TYPE TMC2208_STANDALONE
#else
  #define ALL_DRIVERS_TYPE A4988
#endif
#define X_DRIVER_TYPE  ALL_DRIVERS_TYPE
#define Y_DRIVER_TYPE  ALL_DRIVERS_TYPE
#define Z_DRIVER_TYPE  ALL_DRIVERS_TYPE
//#define I_DRIVER_TYPE  ALL_DRIVERS_TYPE
//#define J_DRIVER_TYPE  ALL_DRIVERS_TYPE
//#define K_DRIVER_TYPE  ALL_DRIVERS_TYPE
//#define X2_DRIVER_TYPE ALL_DRIVERS_TYPE
//#define Y2_DRIVER_TYPE ALL_DRIVERS_TYPE
#define Z2_DRIVER_TYPE ALL_DRIVERS_TYPE
//#define Z3_DRIVER_TYPE ALL_DRIVERS_TYPE
//#define Z4_DRIVER_TYPE ALL_DRIVERS_TYPE
#define E0_DRIVER_TYPE ALL_DRIVERS_TYPE
//#define E1_DRIVER_TYPE ALL_DRIVERS_TYPE
//#define E2_DRIVER_TYPE ALL_DRIVERS_TYPE
//#define E3_DRIVER_TYPE ALL_DRIVERS_TYPE
//#define E4_DRIVER_TYPE ALL_DRIVERS_TYPE
//#define E5_DRIVER_TYPE ALL_DRIVERS_TYPE
//#define E6_DRIVER_TYPE ALL_DRIVERS_TYPE
//#define E7_DRIVER_TYPE ALL_DRIVERS_TYPE

#define SWAPPED_Z_PLUGS

#define TEMP_SENSOR_0 5

#define TEMP_SENSOR_BED 1

//#define PIDTEMP          // See the PID Tuning Guide at https://reprap.org/wiki/PID_Tuning
#define MPCTEMP        // ** EXPERIMENTAL **

  // i3 Mega stock v5 hotend, 40W heater cartridge (3.6Ω @ 22°C)
  #if ENABLED(PID_PARAMS_PER_HOTEND)
    // Specify up to one value per hotend here, according to your setup.
    // If there are fewer values, the last one applies to the remaining hotends.
    #define DEFAULT_Kp_LIST {  15.94,  15.94 }
    #define DEFAULT_Ki_LIST {   1.17,   1.17 }
    #define DEFAULT_Kd_LIST {  54.19,  54.19 }
  #else
    #define DEFAULT_Kp 20.24
    #define DEFAULT_Ki 1.29
    #define DEFAULT_Kd 79.35
  #endif

  #define MPC_EDIT_MENU                             // Add MPC editing to the "Advanced Settings" menu. (~1300 bytes of flash)
  #define MPC_AUTOTUNE_MENU                         // Add MPC auto-tuning to the "Advanced Settings" menu. (~350 bytes of flash)

  // Measured physical constants from M306
  #define MPC_BLOCK_HEAT_CAPACITY { 10.17f }           // (J/K) Heat block heat capacities.
  #define MPC_SENSOR_RESPONSIVENESS { 0.0979f }         // (K/s per ∆K) Rate of change of sensor temperature from heat block.
  #define MPC_AMBIENT_XFER_COEFF { 0.0817f }           // (W/K) Heat transfer coefficients from heat block to room air with fan off.
  #if ENABLED(MPC_INCLUDE_FAN)
    #define MPC_AMBIENT_XFER_COEFF_FAN255 { 0.1269f }  // (W/K) Heat transfer coefficients from heat block to room air with fan on full.
  #endif

    #define MPC_FAN_0_ALL_HOTENDS

#define PIDTEMPBED

// Anycubic i3 Mega Ultrabase (0.9Ω @ 22°C)
  #define DEFAULT_bedKp 251.78
  #define DEFAULT_bedKi 49.57
  #define DEFAULT_bedKd 319.73

#define EXTRUDE_MAXLENGTH 600

#define USE_XMAX_PLUG  // used as the second z stepper end limit switch

// Mechanical endstop with COM to ground and NC to Signal uses "false" here (most common setup).
#define X_MIN_ENDSTOP_INVERTING true // Set to true to invert the logic of the endstop.
#define Y_MIN_ENDSTOP_INVERTING true // Set to true to invert the logic of the endstop.
#define Z_MIN_ENDSTOP_INVERTING true // Set to true to invert the logic of the endstop.

#define X_MAX_ENDSTOP_INVERTING true // Set to true to invert the logic of the endstop.
#define Y_MAX_ENDSTOP_INVERTING true // Set to true to invert the logic of the endstop.
#define Z_MAX_ENDSTOP_INVERTING true // Set to true to invert the logic of the endstop.

#define Z_MIN_PROBE_ENDSTOP_INVERTING DISABLED(I3MEGA_HAS_BLTOUCH) // Set to true to invert the logic of the probe.

#define DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 400, 96.2 }

#define DEFAULT_MAX_FEEDRATE          { 300, 300, 5, 60 }

#define DEFAULT_MAX_ACCELERATION      { 3000, 2000, 60, 10000 }

#define DEFAULT_ACCELERATION                  1500  // X, Y, Z ... and E acceleration for printing moves

#define DEFAULT_EJERK    10.0  // May be used by Linear Advance

//#define Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN

#if DISABLED(I3MEGA_HAS_BLTOUCH)
  #define PROBE_MANUALLY
#endif

#if ENABLED(I3MEGA_HAS_BLTOUCH)
  #define BLTOUCH
#endif

#define NOZZLE_TO_PROBE_OFFSET { 0, -23, -1.54 }

#define MULTIPLE_PROBING 2
#define EXTRA_PROBING    1

#if ENABLED(I3MEGA_HAS_BLTOUCH)
  #define Z_MIN_PROBE_REPEATABILITY_TEST
#endif

#define INVERT_X_DIR true // set to true for stock drivers or TMC2208 with reversed connectors
#define INVERT_Y_DIR false // set to false for stock drivers or TMC2208 with reversed connectors
#define INVERT_Z_DIR false // set to false for stock drivers or TMC2208 with reversed connectors

#define X_BED_SIZE 210
#define Y_BED_SIZE 210

#define X_MIN_POS -5

#define Z_MAX_POS 205

#define FILAMENT_RUNOUT_SENSOR

  #define FIL_RUNOUT_STATE     HIGH    

#if ENABLED(I3MEGA_HAS_BLTOUCH)
  #define AUTO_BED_LEVELING_BILINEAR
#endif
#if DISABLED(I3MEGA_HAS_BLTOUCH)
  #define AUTO_BED_LEVELING_UBL
#endif

  #define G26_MESH_VALIDATION

  #define GRID_MAX_POINTS_X 5
  
#define LCD_BED_LEVELING

#define EEPROM_SETTINGS     // Persistent storage with M500 and M501

#define NOZZLE_PARK_FEATURE

#define SDSUPPORT

#define SDIO_SUPPORT //causes bootloops if not set

#define SD_CHECK_AND_RETRY

#define SPEAKER

#define ANYCUBIC_TFT35

#define TFT_COLOR_UI

#define TOUCH_SCREEN

  //Settings for the I3 Mega Display, when rotated 180° to fix it being upside down.
  #define TOUCH_CALIBRATION_X 17819
  #define TOUCH_CALIBRATION_Y -11849
  #define TOUCH_OFFSET_X -32
  #define TOUCH_OFFSET_Y 344

    #define SINGLE_TOUCH_NAVIGATION


---------------IN CONFIGURATION_ADV.H---------------

#define USE_CONTROLLER_FAN

  #define CONTROLLER_FAN_PIN PD6

#define E0_AUTO_FAN_PIN FAN1_PIN

  #define Z_MULTI_ENDSTOPS

    #define Z2_USE_ENDSTOP   _ZMAX_

    #define SHOW_REMAINING_TIME

      #define ROTATE_PROGRESS_DISPLAY

  #define POWER_LOSS_RECOVERY //untested
  
#define BABYSTEPPING

#define LIN_ADVANCE

  #define LIN_ADVANCE_K 0.8
  
#define MAX_CMD_SIZE 128  
#define BUFSIZE 8

#define TX_BUFFER_SIZE 4

#define RX_BUFFER_SIZE 256

#define EMERGENCY_PARSER

#define ADVANCED_PAUSE_FEATURE

  #define PAUSE_PARK_RETRACT_FEEDRATE         50
  
  #define FILAMENT_CHANGE_UNLOAD_FEEDRATE     30
  
  #define FILAMENT_CHANGE_UNLOAD_LENGTH      555
  
  #define FILAMENT_CHANGE_FAST_LOAD_LENGTH   538
  
  #define ADVANCED_PAUSE_PURGE_LENGTH         60
  
  #define ADVANCED_PAUSE_RESUME_PRIME          2
  
  #define PARK_HEAD_ON_PAUSE
  
#define HOST_ACTION_COMMANDS

  #define HOST_PROMPT_SUPPORT
```
