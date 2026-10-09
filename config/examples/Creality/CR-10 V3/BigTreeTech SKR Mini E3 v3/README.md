# CR-10 V3 with BigTreeTech SKR Mini E3 v3:

## Information

These configuration files were derived from the existing CR-10 v3 Configuration files. Modified to work with the SKR Mini E3 v3.<br />
*NOTE: I don't use the Filament Runout sensor, so its the only thing I have not personally tested here.*

 - BLtouch / CRtouch (Connected to Z-Probe. Requires making custom harness or directly wiring from Z-Probe port to Touch Probe bypassing daughter board)
    - Make your own harness using the 3 pin Z Limit and D11 Pin. Follow this wiring: <br />
    *NOTE: Z Limit Pin 1 is marked on the edge of the connector with a V cutout.* <br />
    - | BTT Z-Probe Pin | Touch Cable Color | CR-10 v3 Pin | Function |
        | -------- | ------- | ------ | ------ |
        | PC14  | Blue | Z Limit Pin 1 | Sensor |
        | Ground | Red | Z Limit Pin 2 | Ground |
        | PA1 | Yellow | D11 | Control | 
        | +5v | Black | Z Limit Pin 3 | Power |
        | GND | White | EMPTY | N/A |

 - Stock LCD (connected to the LCD's EXT3 spare port, with one single straight ribbon cable to EXP1)
 - Stock Titan extruder
 - 3 Pin X Limit connector is for Filament Runout Sensor. Connect to E0-STOP
- Connect Part Cooling Fan to FAN0
 - Connect Hotend \ Extruder Fan to FAN1
 - Connect CR10v3 Case \ Housing Fan to FAN2 (Create or buy a 2 pin Y adapter and connect to this FAN2 connector if you have more than 1 fan in the housing)

## Flashing Mainboard Firmware

The bootloader which handles flashing new firmware on this board remembers the last filename you used.

### Where to put the firmware file on the SDCard:

Put the `firmware.bin` file into the root folder.
