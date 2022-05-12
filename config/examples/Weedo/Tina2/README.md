## Product version

- TINA2 WIFI: TINA2 standard version with ESP32 WIFI module installed. Support remote control, send files via wifi, and online 3d model library.
- TINA2 BASIC: TINA2 lite version, without WIFI module and protective shell.

Please note the monorpice cadet printer is a rebranded version of these printers and the provided configuration should work.

## Hardware version

- V2: The motherboard version is 62AS. The endstop type is lever limit switch.
- V3: The motherboard version is 62AS. The endstop type is mushroom head limit switch.

## Adding wifi support using ESP3D

You can add wifi support using [ESP3D](https://github.com/luc-github/ESP3D).  
Basically connect your own NodeMCU to second serial port of the MCU.  
See ESP3D wiki for connection diagram.

In Marlin configuration.h set:  
`#define SERIAL_PORT_2 3`

## Manufacturer wifi support

Examples provided here have not been tested with wifi board from manufacturer.  
Setting `#define SERIAL_PORT_2 3` in Marlin configuration.h might be enough to work with manufacturer wifi board.

Feedback are welcome.
