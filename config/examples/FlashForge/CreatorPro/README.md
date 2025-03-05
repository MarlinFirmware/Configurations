# FlashForge Creator Pro

> [!IMPORTANT]
> **NOTE ON FLASHING THE FIRMWARE:**
> The Mightyboard uses an Arduino Mega bootloader but it doesn't do an automatic reset on DTR. To make the printer reset on DTR you'll need to flash it with a standard (or other) Arduino Mega bootloader.
>
> See [this guide](https://github.com/felipeksw/CreatorPro-Marlin-Cura/tree/main/Bootloader) for instructions on how to flash the bootloader.

## Machine Settings

- Build plate shape: Rectangular
- Origin at center: No
- Heated bed: Yes
- G-code flavor: Marlin
- Number of Extruders: 2
- X (Width) 227
- Y (Depth) 148
- Z (Height) 150

### Extruder 1 (Right)

- Nozzle size: 0.4
- Compatible material diameter: 1.75
- Nozzle offset X: 0
- Nozzle offset Y: 0
- Cooling Fan Number: 0

### Extruder 2 (Left)
- Nozzle size: 0.4
- Compatible material diameter: 1.75
- Nozzle offset X: 0 (-34mm offset handled via firmware)
- Nozzle offset Y: 0
- Cooling Fan Number: 0

## G-code

Add this G-code to your slicer (ex. Ultimaker Cura) or print server (ex. OctoPrint).

### Before Print Job Starts

```gcode
M118 Starting print...
M300 S880 P500
M300 S660 P200
M300 S1300 P200
M300 S880 P500

; Set temperatures
M104 T0 S{material_print_temperature, 0}
M104 T1 S{material_print_temperature, 1}
M140 S{material_bed_temperature}
; Home printer
G28
; Purge right nozzle
T0
G0 X270 Y0 Z30 F4800
M190 S{material_bed_temperature}
M109 T0 S{material_print_temperature, 0}
M104 T0 S{material_standby_temperature, 0}
G92 E0
G0 Z0.4 F1800
G1 X225 Y0 E20 F300 ; purge nozzle
G0 X235 Y0 Z0.15 F1200 ; slow wipe
G1 E17 F2400
G0 X225 Y0 Z0.5 F1200 ; lift
G92 E0
; Purge left nozzle
T1
;M104 T0 S{material_standby_temperature, 0}
M104 T1 S{material_print_temperature, 1}
G0 X0 Y0 Z30 F4800
M109 T1 S{material_print_temperature, 1}
G92 E0
G0 Z0.4 F1800
G1 X48 Y0 E25 F300 ; purge nozzle
G0 X38 Y0 Z0.15 F1200 ; slow wipe
G1 E22 F3600
G0 X48 Y0 Z0.5 F1200 ; lift
G0 Y-10 ; Move nozzle off of build plate
G92 E0
M106 ; Start turbo fan
```

### After Print Job Completes

```gcode
M118 Print complete!
M300 S440 P200
M300 S660 P200
M300 S880 P200
M300 S1300 P200
M300 S880 P500

G10 ; Retract
G0 X270 Y150 Z150 F1500 ; Send Z axis to bottom of machine

; Disable all heaters
{% snippet 'disable_hotends' %}
{% snippet 'disable_bed' %}

M107 ; Stop turbo fan
M18 ; Disable stepper
G11
```

### After Print Job is Cancelled

```gcode
M118 Print aborted!
M300 S1300 P200
M300 S880 P200
M300 S660 P200
M300 S440 P200

G10 ; Retract
G0 X270 Y150 Z150 F1500 ; Send Z axis to bottom of machine

; Disable all heaters
{% snippet 'disable_hotends' %}
{% snippet 'disable_bed' %}

M127 ; Stop turbo fan
M18 ; Disable stepper
G11
```

### Before Tool Change

```gcode
; Retract filament
G10
G10 S1

; Move Z-axis slightly
G91
G0 Z1
G90
```

### After Tool Change

```gcode
; Un-retract filament
G11
G11 S1

; Move Z-axis back
G91
G0 Z-1
G90
```

## Tips

### My nozzles are not offset in firmware!

It's possible that you may have different offsets saved in your printer's EEPROM. To fix this, you can either update your offset settings in the printer's configuration panel, or you can run the following G-code:

```gcode
M218 T1 X-34 ; Set the offset
M500 ; Save settings to EEPROM
```
