# Creality Ender-5 S1 — CR10 Stock Display (MarlinUI)

This configuration uses the Creality / CR-10 12864 knob display (`CR10_STOCKDISPLAY`, ST7920) with the full MarlinUI menu system in place of the stock touch screen. For the stock touch screen, see the [Touch Screen](../Touch%20Screen) configuration.

## Wiring

The display plugs into the 10-pin header labeled "LCD" on the CR4NS200141C13 board. This is the same EXP3 layout as the Creality V4.x and Ender-3 S1 boards:

```
          ------
    PC6  | 1  2 | PB2
    PA2  | 3  4 | PA3
    PB14   5  6 | PB13
    PB12 | 7  8 | PB15
     GND | 9 10 | 5V
          ------
           EXP3
```

| Header pin | Signal | MCU pin |
| --- | --- | --- |
| 1 | `BEEPER_PIN` | PC6 |
| 2 | `BTN_ENC` | PB2 |
| 3 | `BTN_EN1` | PA2 |
| 5 | `BTN_EN2` | PB14 |
| 6 | `LCD_PINS_D4` (clock) | PB13 |
| 7 | `LCD_PINS_RS` (chip select) | PB12 |
| 8 | `LCD_PINS_EN` (data) | PB15 |

Pins 3 and 4 are UART2 (PA2/PA3) for the touch screen, so `CREALITY_RTS`, `CREALITY_WIFI` and `MENU_RESET_WIFI` are not used with this configuration.

The display, knob, button and beeper were checked on an Ender-5 S1 with the original touch screen still connected.

## Differences from the Touch Screen configuration

- `CR10_STOCKDISPLAY` replaces `CREALITY_RTS`.
- The ST7920 serial timing is slowed to 600 ns in the board's pins file (`BOARD_ST7920_DELAY_1/2/3`). With the default 125 ns this MCU leaves the display blank.
- More menu items: Info (About) screen, Marlin boot screen, scrolling status messages and long file names, sorted SD card list, Bed Leveling menu, Probe Offset Wizard, sound (mute) item, return to the status screen after 15 seconds, and double-click for Z babystepping.
- The Creality-only identity strings (firmware, screen and hardware versions, website) are omitted because only the touch screen shows them.

## Installing

The bootloader on the stock board has special requirements and requires a flag to be set in the EEPROM before it will install the firmware.

- The built firmware bin file must be placed into a folder named `STM32F4_UPDATE` on the SD card.
- Connect to the printer over serial and send `M936 V2`. (You can also run a G-code file containing `M936 V2`.)
- Make sure to always flash a working version of Marlin with `OTA_FIRMWARE_UPDATE` enabled!
- If for any reason you can't run `M936 V2` then you'll need to run a sketch to write 0x01 to EEPROM address 90 (e.g., with `BL24CXX::write`). (A value of 0x02 selects the screen update instead; that is what `M936 V3` sets.)

## Notes

- Other Marlin options (such as `LCD_BED_TRAMMING` and `ASSISTED_TRAMMING`) need positions chosen for your bed and probe, so they are left off.
- Acceleration and jerk are conservative starting values and have not been tuned.
