## Product version

There are several versions with different hardware

- **TINA2 WIFI / TINA2 BASIC**
    - Outdated older models
    - Called V2/V3 hardware by the manufacturer (weedo/weefun/entina?)
    - TINA2 WIFI -- TINA2 standard version with ESP32 WIFI module installed. Support remote control, send files via wifi, and online 3d model library.
    - TINA2 BASIC -- TINA2 lite version, without WIFI module and protective shell.
    - Uses motherboard R62A/R62AS with ATMEGA2560 MCU.
    - Firmware files are 8-bit, identified by the .hex extension
    - [Official TINA2firmware repo](https://github.com/weedo3d/TINA2firmware)

- **TINA2 UPGRADE**
    - V7 hardware
    - Current "basic" model. Sometimes called TINA2 or TINA2 BASIC, which adds to the confusion
    - Uses motherboard R72A/R72B with GD32F103RET6 MCU
    - Firmware files are 32-bit, identified by the .bin or .wfm (their proprietary format). These firmware files are NOT compatible with the older ATMEGA2560-based models, or vice versa. If your firmware update fails, it may well be due to this mismatch.
    - [Official Tina2Upgradefirmware repo](https://github.com/weedo3d/Tina2Upgradefirmware)

- **TINA2S**
    - Current "wifi" model. Compared to the base TINA2 UPGRADE model, adds wifi and heated bed.
    - Uses motherboard R72H/R72P with GD32F103RET6 MCU
    - [Official TINA2Sfirmware repo](https://github.com/weedo3d/TINA2Sfirmware)

> [!NOTE]
> The Monorprice cadet printer is a rebranded version of the V2/V3 printers and the provided configuration should work.

## Hardware version

- V2: The motherboard version is 62AS. The endstop type is lever limit switch.
- V3: The motherboard version is 62AS. The endstop type is mushroom head limit switch.
- V7: The motherboard version R72*. The endstop type is mushroom head limit switch.

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

## Manufacturer usb support

All printers use CH340/CH341 for USB. The driver is often included as part of official driver releases.
[The latest version is also available from the chip manufacturer](https://www.wch.cn/download/CH341SER_EXE.html)
