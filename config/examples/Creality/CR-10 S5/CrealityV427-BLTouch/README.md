The 427 board needs the following hardware mods to work with the CR-10 S5:
- Somehow attach both Z-motors to a single socket (increase power using the onboard screws?)
- filament sensor doesn't work, yet. The only socket left near the endstops is correct.
- connect display with a single cable to EXT3

The BL touch got it's own socket. For it to work remove the Z-Endstop cable from it's socket.

Autleveling the bed
from https://marlinfw.org/docs/features/unified_bed_leveling.html

M190 S50        ; Set bed temp to 50C recommended for accuracy when using a heated bed
M104 S200       ; Set nozzle temp to 200C recommended for accuracy when using nozzle to probe

G28             ; Home XYZ.
G29 P1          ; Do automated probing of the bed.
G29 P2 B T      ; Manual probing of locations. (USUALLY NOT NEEDED!)
G29 P3 T        ; Repeat until all mesh points are filled in.

G29 T           ; View the Z compensation values.
G29 S0          ; Save UBL mesh points to slot 0.
G29 F 10.0      ; Set Fade Height for correction at 10.0 mm.
G29 A           ; Activate the UBL System.
M500            ; Save settings to EEPROM.
                ; WARNING: Causes UBL to be active at power-up, before any G28.

Mesh Fine-Tuning
G26 C P5.0      ; Produce mesh validation pattern (G26), continue with closest point (C), prime nozzle by extruding 5mm (P5.0), 
                ; set filament diameter 3mm (F3.0), S0.4 for nozzle size
                ; temperatures are assumed as set in config. unless you specify, e.g., B105 H225 for ABS Plastic
G29 P4 T        ; Move nozzle to 'bad' areas and fine tune the values if needed
                ; Repeat G26 and 'G29 P4 T' commands as needed.

G29 S0          ; Save UBL mesh values to slot 0.
M500            ; Save settings to EEPROM.

Transform Mesh with 3-Point Probing - fast init on print start
G29 L0          ; Load UBL mesh values from slot 0.
G29 J           ; Probe 3 points and tilt the mesh to the plane.
                ; This can be useful in the starting G-code of your preferred slicer.

Use M290 command to set the Z offset between probe and nozzle. Needs some experimenting
Negative values result in the nozzle being closer to the bed. Values are relative. 
So try to add or remove on 0.1 mm steps
M290 Z-0.1
M500            ; save when finished

TODO Filamentsensor
TODO Print pause move head, does not return to printing position
TODO before home lift Z
TODO Click to resume
TODO G29 J tilt mesh by measuring 3 points.
