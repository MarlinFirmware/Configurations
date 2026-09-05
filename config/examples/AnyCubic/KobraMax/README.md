# Anycubic Kobra Max

Printer: **Anycubic Kobra Max**
Board: **Trigorilla F1 V1** (HC32F460PETB, 100-pin)
Bed: 400 × 400 mm
Z Height: 450 mm
Probe: Nozzle-as-probe with PROBE_TARE (strain-gauge style)
Display: ANYCUBIC_LCD_KOBRA (serial port 2)
Drivers: TMC2208 (standalone mode) on X, Y, Z, E0

## Notes

- Uses `NOZZLE_AS_PROBE` with `PROBE_TARE` (strain-gauge auto-leveling).
- Input shaping enabled: X=27.88 Hz, Y=50.98 Hz (tune with M593).
- Linear Advance K=0.25 (tune with M900).
- Auto Bed Leveling: Bilinear with subdivision.
- Firmware retraction enabled (6 mm / 45 mm/s).

## References

- Original port: https://github.com/maikramer/MarlinKobraMax
- Marlin PR: MarlinFirmware/Marlin (bf2_anycubic_kobra_max_PR)
