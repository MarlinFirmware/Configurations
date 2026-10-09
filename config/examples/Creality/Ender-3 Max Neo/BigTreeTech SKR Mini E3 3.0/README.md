# Ender-3 Max Neo with BigTreeTech SKR Mini E3 V3.0 Configuration

## DIAG Jumpers

> [!WARNING]
> **Critical Configuration Notes**<br/>The motherboard’s DIAG jumpers must be removed when using end‑stops.

Remove the jumpers outlined in this image:
![DIAG Jumpers](<images/DIAG jumpers.png>)

## LCD Wiring Modification

> [!WARNING]
> The `DWIN_CREALITY_LCD` requires wiring modification!<br/>See `pins_BTT_SKR_MINI_E3_V3_0.h` for details. Requires a custom cable.

### Physical Layout
```
Board and display pin layouts
        ------                ------
   ENT | 1  2 | BEEP      5V | 1  2 | GND
   TX1 | 3  4 |            A | 3  4 | B
   RX1   5  6 |         BEEP | 5  6   ENT
     B | 7  8 | A         TX | 7  8 | RX
   GND | 9 10 | 5V           | 9 10 |
        ------                ------
  Motherboard EXP1        Screen connector
```

### Pin Connections
| Motherboard | Screen |
|-------------|--------|
| TX1         | RX     |
| RX1         | TX     |
| BEEP        | BEEP   |
| A           | A      |
| B           | B      |
| 5V          | 5V     |
| GND         | GND    |
