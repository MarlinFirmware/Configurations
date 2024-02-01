## Product version

There are several versions of the Weedo TINA2 with different hardware.

### TINA2 WIFI / TINA2 BASIC
- Outdated older models.
- Called V2/V3 hardware by the manufacturer (Weedo / Weefun / Entina?).
- The TINA2 WIFI is the standard TINA2 with ESP32 WIFI module installed. Supports remote control, sending files via WiFi, and online 3D model library.
- The TINA2 BASIC is the lite version of the TINA2 with no WiFi module or protective shell.
- Uses motherboard R62A/R62AS with ATMEGA2560 MCU.
- Firmware files are 8-bit, identified by the "`.hex`" extension.
- [Official TINA2firmware repo](https://github.com/weedo3d/TINA2firmware)

### TINA2 UPGRADE
- V7 hardware.
- Current "basic" model. Sometimes called TINA2 or TINA2 BASIC, which adds to the confusion.
- Uses motherboard R72A/R72B with a GD32F103RET6 MCU.
- Firmware files are 32-bit, identified by the "`.bin`" or "`.wfm`" extension (proprietary format). These firmware files are NOT compatible with the older ATMEGA2560-based models, or vice versa. If your firmware update fails, it may be due to this mismatch.
- [Official Tina2Upgradefirmware repo](https://github.com/weedo3d/Tina2Upgradefirmware)

### TINA2S
- Current "WiFi" model. Compared to the base TINA2 UPGRADE model, adds WiFi and a heated bed.
- Uses motherboard R72H/R72P with a GD32F103RET6 MCU.
- [Official TINA2Sfirmware repo](https://github.com/weedo3d/TINA2Sfirmware)

> [!NOTE]
> The "Monoprice Cadet" is a rebranded version of the V2/V3. The provided configuration should work.

## Hardware identification

- V2: Motherboard version 62AS. The endstop is a lever limit switch.
- V3: Motherboard version 62AS. The endstop is a mushroom head limit switch.
- V7: Motherboard version R72*. The endstop is a mushroom head limit switch.

## Adding WiFi support using ESP3D

You can add WiFi support using [ESP3D](https://github.com/luc-github/ESP3D).
Basically connect your own NodeMCU to second serial port of the MCU.
See the [ESP3D wiki](http://esp3d.io/esp3d/) for connection diagrams.

In `Configuration.h` set:
```c
#define SERIAL_PORT_2 3
```

## Manufacturer WiFi support

The provided example configurations have not been tested with the WiFi board from the manufacturer.
Setting `#define SERIAL_PORT_2 3` in `Configuration.h` might be enough to work with the manufacturer WiFi board.

Feedback is welcome.

## Manufacturer USB support

All printers use CH340/CH341 for USB. The driver is often included as part of official driver releases.
[The latest version is also available from the chip manufacturer](https://www.wch.cn/download/CH341SER_EXE.html)
