# BigTreeTech BTT002/TMC2209 Config for Prusa MK3S

## Requirements
- [Prusa MK3S](https://www.prusa3d.com/original-prusa-i3-mk3/) or MK3 with MK3S upgrade
- BigTreeTech BTT002 motherboard
- 4 x TMC2209s

## Upgrade Notes
* Cut or desolder the Z & E driver DIAG pins or they will interfere with PINDA & filament runout detection.
* Set the jumpers under your drivers to "TMC2208-UART MODE":
![image](https://user-images.githubusercontent.com/13375512/74117621-24415000-4b6d-11ea-8811-f867e187ea0c.png)

## Known Issues
* Save/send `M500` twice or `EEPROM_SETTINGS` won't stick on reboot.
