# Ender 3 Pro Configurations for SKR 1.4 Turbo with TMC2209 Bugfix CONFIGURATION_H_VERSION 020008

This configuration is for an Ender 3 Pro with the following options enabled:
- Motherboard BigTreeTech SKR 1.4 Turbo
- Drivers TMC2209 (sensorless homing enabled)
- BLtouch Bed leveling Sensor (Bilinear Mode 5x5 Grid) (sensor plugged into the probe pins)
- Auto Fillament Load and unload enabled (measure your bowden length + extruder up to nozzle and change values FILAMENT_CHANGE_UNLOAD_LENGTH and FILAMENT_CHANGE_FAST_LOAD_LENGTH)
- Linear Advance enabled (Do a calibration for your correct values)
- TFT 35V3 (EXP3 + TFT cables using #define CR10_STOCKDISPLAY or change it to #define REPRAP_DISCOUNT_FULL_GRAPHIC_SMART_CONTROLLER and use EXP1 and EXP2)
- Extruder Auto Fan at 50C (Extruder Fan connected to Pin P2_04 HE1)

I may have some other options enabled that i dont remember, be careful to check everything that corresponds to your machine.
