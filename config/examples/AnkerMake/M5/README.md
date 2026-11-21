# AnkerMake M5

Example configuration for the AnkerMake M5 (model V8111) with its stock V8111 mainboard (STM32F407VGT6 or GD32F407VGT6).

Settings come from AnkerMake's own Marlin release (V3.0.75, https://github.com/ankermake/AnkerMake-Marlin), translated to current Marlin options.

## Status: experimental, not ready for printing

Support for this machine is a work in progress. Know these limits before flashing:

- **Hotend:** on newer toolheads the hotend heater and thermistor are run by the toolhead's own "nozzle board" over a serial link. Marlin doesn't talk to the nozzle board yet, so the hotend won't heat on those toolheads, and Marlin will likely stop with a MINTEMP error.
- **Probe:** the bed probe is a strain gauge in the nozzle board. It has to be zeroed over the same serial link, so probing, Z homing and bed leveling are not expected to work yet.
- **Host and app:** the printer's built-in Linux host (touch screen, AnkerMake app, slicer upload) speaks AnkerMake's own protocol. It will not work with this firmware yet.
- **Thermistors:** AnkerMake's firmware used modified copies of thermistor tables 5 and 1. This example uses Marlin's standard tables, so temperature readings may differ slightly.

## Flashing: no way back to stock

AnkerMake only updates the printer over the cloud (OTA). Installing Marlin means opening the printer and flashing the mainboard over SWD with an ST-Link or similar.

> [!WARNING]
> The stock MCU is reported to be read-protected, so the stock firmware can't be backed up. Removing the protection erases the whole chip, including AnkerMake's bootloader. After that the printer can't return to the stock firmware, and AnkerMake's OTA updates will no longer reach the mainboard.

Marlin is built to run from the start of flash (0x08000000) with no bootloader. Build with the `STM32F407VG_ankermake` environment.

## Serial

- `SERIAL_PORT 1` (USART1, PA9/PA10) at 115200 baud. Community reports say these pins are on a header on the mainboard.
- `SERIAL_PORT_2 3` (USART3, PD8/PD9) at 1,000,000 baud. This port goes to the printer's Linux host.

## Notes

- X and Y home with sensorless homing (TMC2209 StallGuard). Y homes to max.
- The two Z motors are aligned with `G34` (`Z_STEPPER_AUTO_ALIGN`).
- `LIN_ADVANCE` uses AnkerMake's K value (0.06). Recalibrate it for Marlin's Linear Advance.
