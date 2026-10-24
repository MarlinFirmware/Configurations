# Replicator 2 configuration 

Features:
- Single extruder
- Type K thermocouple
- No heat bed
- Print Area 250mm x 150mm 
- Mightyboard interface (Shift register)
- RGB LED (PCA9632) at addresses 0x62 and 0x70 (all call 0xE0 > 1)

Board: Mightyboard 2, also known as Mightyboard revision G/H
- micro: Atmega1280
- ADS1118 and thermocouples (software SPI)
- Digitpots (software i2C for each at address 0x2F)
- A49888 Motor drivers 

- Flashing: USB or ISP
