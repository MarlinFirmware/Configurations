# Instructions

* A modified cable is needed for the Knob display, connections in [link](https://www.smith3d.com/skr-mini-e3-v2-v3-on-ender-3-v2-ender-3-s1-lcd-dwin-knob-screen/)
* How to flash [display](https://3dprinting.stackexchange.com/questions/21729/how-to-successfully-flash-a-dacai-lcd-screen-of-a-creality-ender-3-v2)

## Bill of materials
BTT SKR mini E3 V3.0
LCD DWIN knob screen

#Notes
* Based of `config/examples/Creality/Ender-3\ V2/BigTreeTech\ SKR\ Mini\ E3\ 3.0/MarlinUI/`

# Communication with the printer using USB
```
minicom -D /dev/ttyACM0 -b 115200
```
How to get nicer output in minicom
```
ctrl-A Z
local Echo on/off..E
Add Carriage Ret...U
```

## Gcode reference
`M43` debug pin, needs to enable in firmware.
`M43 P0 S` Servo probe test
`M280 P0 S120` CR-touch self test.



# References
* https://www.smith3d.com/skr-mini-e3-v2-v3-on-ender-3-v2-ender-3-s1-lcd-dwin-knob-screen/
* https://github.com/bigtreetech/BIGTREETECH-SKR-mini-E3/blob/master/hardware/BTT%20SKR%20MINI%20E3%20V3.0/Hardware/BTT%20SKR%20MINI%20E3%20V3.0%20user%20manual.pdf
* https://github.com/bigtreetech/BIGTREETECH-SKR-mini-E3/tree/master/hardware/BTT%20SKR%20MINI%20E3%20V3.0
* https://github.com/MarlinFirmware/Marlin/issues/27124
* https://www.reddit.com/r/ender3v2/comments/1cguk2b/cr_touch_z_axis_not_homing_marlin_firmware/
* https://www.reddit.com/r/BIGTREETECH/comments/rnsopr/skr_mini_e3_v30_crtouch_zhoming_issue

