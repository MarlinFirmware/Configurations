# Ender-3 Max Neo with BigTreeTech SKR Mini E3 V3.0 Configuration

> **⚠️ WARNING: Critical Configuration Notes**

## DIAG Jumpers

> **Warning**
> Motherboard DIAG jumpers must be removed when using endstops.

Remove these jumpers:
![DIAG Jumpers](<README images/DIAG jumpers.png>)

## DWIN_CREALITY_LCD Wiring Modification

> **WARNING!**
> DWIN_CREALITY_LCD requires wiring modification! See `pins_BTT_SKR_MINI_E3_V3_0.h` for details (replicated below). Requires a custom cable.

```
        ------                ------
   ENT | 1  2 | BEEP      5V | 1  2 | GND
   TX1 | 3  4 |            A | 3  4 | B
   RX1   5  6 |         BEEP | 5  6   ENT
     B | 7  8 | A         TX | 7  8 | RX
   GND | 9 10 | 5V           | 9  10|
        ------                ------
  Motherboard EXP1        Screen connector
```
As layed out on the physical boards


Connect the following pins:

| Motherboard | Screen |
|-------------|--------|
| TX1         | RX     |
| RX1         | TX     |
| BEEP        | BEEP   |
| A           | A      |
| B           | B      |
| 5V          | 5V     |
| GND         | GND    |
