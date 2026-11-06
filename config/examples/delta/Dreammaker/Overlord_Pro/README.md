# Dreammaker Overlord Pro

Overlord Pro needs larger PSU than stock PSU. Uncomment `#define OVERLORD_PRO_UPGRADED_PSU` to enable heated bed.

## Details

The hotend heater is 24V 60W, bed is 24V 160W, standard Overlord Pro PSU is 24V 220.8W.

Hotend and bed are PWMed to keep their average power less than the max power but they can both be on at the same time.

If both are on at the same time, then there is no power available for anything else and power supply will shutdown if steppers are moving while both hotend and bed are on.

## Recommend PSU

A Meanwell RSP-500-24 works, a RSP-350-24 should work but has not been tested.