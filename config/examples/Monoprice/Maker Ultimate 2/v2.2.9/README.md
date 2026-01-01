> Modified manufacturer config running much closer to stock Marlin found here: [OstlerDev/Marlin_MonopriceUltimate2](https://github.com/OstlerDev/Marlin_MonopriceUltimate2)
> Also requires the board and pin files in the parent folder.
> *VZ 20260101*
....................

# Marlin2_MonopriceUltimate2

Note: This fork tracks upstream Marlin 1.1.x for critical fixes. Upstream docs: [Marlin 1.1.x](https://github.com/MarlinFirmware/Marlin/tree/1.1.x).
Original Manufacturer Firmware: https://github.com/WEEDO3DTECH/MonopriceUltimate2_Marlin

Monoprice Ultimate2 firmware base on <a href="https://github.com/MarlinFirmware/Marlin/tree/1.1.x" target="_blank">Marlin 1.1.x</a>  
  
## Releases
### V 3.0.0 (Marlin 1.1.9.2)
* Pulled in bugfixes from Marlin 1.1.9 -> 1.1.9.2
* Support for Mesh 3x3 Auto Bed Leveling instead of just 3 point ABL
* Stock Marlin UI navigation!
* Only kept machine settings, tossed out all the manufacturer bullshit.
* Enabled Z_SAFE_HOMING

If you run into issues with disconnects after flashing, clear your EEPROM (`M502` then `M500`) so saved defaults don’t fight the new versions config.

### V 2.2.8 (Marlin 1.1.9)
* Ultimate2 V2 factory firmware
* Integration of Chinese, Japanese, English, French, German, Spanish and Italian languages, online dynamic switching.
* Improved filament auto feed and retract functions, with dedicated interface and voice prompt.
* Added stepper motor off function to prepare menu.
* Added nozzle parking function when printing is paused.
* Improved the Z-axis offset adjustment function.
* Added the wizard function launched by first power on or restore.
* Added switch options for runout sensor and front door sensor to the TUNE menu when printing.
* Add boot sound prompt.
* Serial port baud rate changed to 115200bps.
* Added a selecting z-axis height menu before goto bed leveling menu. Ultimate2 V1 version corresponds to 165mm. Ultimate2 V2 version corresponds to 170mm. 

### V 1.6
* Ultimate2 V1 factory firmware


