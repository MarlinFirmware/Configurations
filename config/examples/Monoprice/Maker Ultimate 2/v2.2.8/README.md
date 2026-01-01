> Unmodified manufacturer config corresponding to official V2.2.8 firmware found here: [Weedo3D Monoprice Ultimate 2](https://github.com/WEEDO3DTECH/MonopriceUltimate2_Marlin)
> Note that there are other modifications to the Marlin source code (in Weedo3D repo) that are not included here.
> Some functions such as the door sensor are not implemented in Marlin, and these files may not build as-is.
> This is strictly for posterity of the base machine definition.
> At the least it requires the board and pin files in the parent folder.
> *VZ 20260101*
....................

# MonopriceUltimate2_Marlin

Monoprice Ultimate2 firmware base on <a href="https://github.com/MarlinFirmware/Marlin/tree/1.1.x" target="_blank">Marlin 1.1.x</a>  
  
## Releases
### V 2.2.8
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


