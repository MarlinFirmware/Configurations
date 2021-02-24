NOW MKS has a V1.1 Version of MKS Board 

Need to compile using another board pin
the new definition for V1.1 is
#define MOTHERBOARD BOARD_MKS_ROBIN_E3_V1_1 instead   #define MOTHERBOARD BOARD_MKS_ROBIN_E3
changes in the new version:
Z-STEP signal change to PC14
Z-DIR signal change to PC15
Add support AT24C32D eeprom on the board

MKS E3 New hardware can be found here
https://github.com/makerbase-mks/MKS-Robin-E3-E3D/tree/master/hardware
