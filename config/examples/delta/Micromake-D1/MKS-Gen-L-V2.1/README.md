# Micromake D1 → MKS Gen L V2.1
## Configuration & wiring guide

- **Board**: [Makerbase MKS Gen L V2.1](https://github.com/makerbase-mks/MKS-GEN_L/wiki/MKS_GEN_L_V2)  
- **Display**: RepRapDiscount Smart Controller (LCD 2004, 20×4)
- **Drivers**: TMC2209 @ 1⁄16 µ‑step (UART mode)
- **Features**: Single Extruder, Heated bed, Fixed Z‑probe, Dual Fans

### 1. About these configurations
- `Configuration.h` & `Configuration_adv.h` already tuned for Micromake D1 geometry.  
- English 20×4 LCD presets.  
- Safe temperature limits (270°C hot‑end / 120°C bed).  
- Smart auto‑fan on MOSFET D.  
- Updated motion limits for faster homing (100mm/s).  
- EEPROM, SD‑card, auto‑delta‑calibration G33 ready.

### 2. Compare to Anycubic Kossel config

See `config/examples/delta/Anycubic/Kossel`

### 3. Pin correspondence (old board → new)

| Function           | Makeboard Mini 2.1.2 | MKS Gen L V2.1           |
|--------------------|----------------------|--------------------------|
| X‑STEP / DIR / EN  | 54 / 55 / 38         | X.STEP / X.DIR / X.EN    |
| Y‑STEP / DIR / EN  | 60 / 61 / 56         | Y.STEP / Y.DIR / Y.EN    |
| Z‑STEP / DIR / EN  | 46 / 48 / 62         | Z.STEP / Z.DIR / Z.EN    |
| E0‑STEP / DIR / EN | 26 / 28 / 24         | E0.STEP / E0.DIR / E0.EN |
| X‑MAX              | pin 2 (E4)           | X+ JST                   |
| Y‑MAX              | pin 15 (J0)          | Y+ JST                   |
| Z‑MAX              | pin 19 (D2)          | Z+ JST                   |
| Z‑MIN / Probe      | pin 18 (D3)          | Z‑ JST                   |
| Heater‑0           | D10                  | HE0 screw                |
| Bed Heater         | D8                   | BED screw                |
| Thermistor‑0 / Bed | A13 / A14            | TH0 / THB                |
| Fan 0 (model)      | D9                   | FAN screw                |
| Fan 1 (hot‑end)    | D7                   | MOSFETD                  |
| VIN                | XT‑30                | 2‑pin 12–24V in          |
