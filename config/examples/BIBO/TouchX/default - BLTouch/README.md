Note: Users with factory mks tf28 screens will need to modify the screen baudrate to 115200. 
The factory baudrate of 250000 causes problems with gcode items which report back information like M114. 
Using 115200 on both the mainboard and the screen resolves this issue.

Change the mks_config.txt configuration file baudrate to cfg_baud_rate:3
This will set the correct baudrate for the screen to match the main board
