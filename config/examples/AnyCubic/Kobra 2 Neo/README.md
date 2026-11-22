# Anycubic Kobra 2 Neo

Printer: **Anycubic Kobra 2 Neo**
Board: **Trigorilla Gen V4.0.1** (GD32F303RGT6, 1 MB flash, 96 KB RAM)
Bed: 220 × 220 mm
Z Height: 250 mm
Probe: Inductive, `NOZZLE_TO_PROBE_OFFSET { 24, 13.35, 0 }`
Display: ST7789 320x240 SPI, `TFT_COLOR_UI` (SPI mode 3, `TFT_MIRROR_Y`)
Drivers: Step/dir drivers configured as A4988 (standalone mode)
Host serial: USART1, 115200 baud
Bootloader: 0x9000, updated from SD card with a file named `firmware.bin`

## Notes

- Settings are stored in the last 4 KB of flash bank 0
  (`FLASH_EEPROM_EMULATION`). `SDCARD_EEPROM_EMULATION` is available as an
  alternative in the pins file.
- The Anycubic SD-card updater only accepts a file named exactly
  `firmware.bin`.
- Classic jerk is used, matching the stock firmware (10 / 10 / 0.3 / 5).
- Linear Advance K = 0.02 (tune with `M900`).
- Input shaping enabled: X = 55.77 Hz, Y = 52.70 Hz (tune with `M593`).
- Bilinear ABL with a 5×5 grid; Z homing uses the probe with `Z_SAFE_HOMING`.
- X/Y travel is `BED_SIZE + 10` to match the stock firmware.
- Hotend heatsink fan on FAN1 (`E0_AUTO_FAN_PIN`), controller fan on FAN2.
- The vendor's proprietary automatic Z-offset module is not ported; standard
  bilinear ABL is used instead.

## References

- Vendor firmware: https://github.com/ANYCUBIC-3D/Kobra2_Neo
- Hardware notes: https://1coderookie.github.io/Kobra2NeoInsights/hardware/mainboard/
