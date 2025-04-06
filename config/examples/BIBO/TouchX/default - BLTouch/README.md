Note: Users with factory mks tf28 screens will need to modify the screen baudrate to 115200. 
The factory baudrate of 250000 causes problems with gcode items which report back information like M114. 
Using 115200 on both the mainboard and the screen resolves this issue.

Change the mks_config.txt configuration file for BLTouch and correct baud rate

set baudrate to 115200
cfg_baud_rate:3

enable auto leveling
cfg_leveling_mode:1
cfg_auto_leveling_cmd:G28;G29;

Enable function of babysteps.
cfg_babystep_btn_display:1
