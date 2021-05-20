## SKR 1.4 Board  

To compile Marlin for this board set `MOTHERBOARD` to `BOARD_BTT_SKR_V1_4`  

Features included:
- BLTOUCH
- TMC 2208
- ADVANCED_PAUSE (for M600)
- NOZZLE PARK

# Important  

It is necessary to adjust the NOZZLE_TO_PROBE_OFFSET according to the configuration of your sensor, this example is based on this sensor support for ender 3: https://www.thingiverse.com/thing:3584158

# Important 2 

This firmware is prepared for you no longer want to use the endstop on the Z axis and want to use BLTOUCH for this feature using dedicated port.