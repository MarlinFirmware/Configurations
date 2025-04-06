# Important User Note:

Users with factory MKS TFT28 screens will need to modify the screen baudrate to 115200. 
The factory baudrate of 250000 causes problems with gcode items that report back information like M114. 
Using 115200 on both the mainboard and the screen resolves this issue.

Change the mks_config.txt configuration file for BLTouch and correct the baud rate, set auto leveling, and enable babysteps
Link to MKS TFT28 screen firmware
https://github.com/makerbase-mks/MKS-TFT/tree/master/MKS-TFT2.8-3.2

### Important mks_config.txt configuration changes
- set baudrate to 115200
  - cfg_baud_rate:3

- Enable auto leveling
  - cfg_leveling_mode:1
  - cfg_auto_leveling_cmd:G28;G29;

- Enable function of babysteps.
  - cfg_babystep_btn_display:1
