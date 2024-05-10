; Intro
M118 E1 Due to the limited number of characters on the FlashForge Creator Pro,
M118 E1 the full plate leveling instructions will be displayed here.
M117 View console for
M300 S880 P50
G4 P50
M300 S880 P50
G4 S1
M117 full directions
G4 S1
M117 View console for
G4 S1
M117 full directions
G4 S1

; Home extruders and build plate
M117 Homing...
G28
T0

; Instruct user to grab a sheet of paper
M118 E1 Grab a sheet of paper, which we will use to measure the distance
M118 E1 between the build plate and the nozzle. We'll move to a few
M118 E1 locations and adjust the turn screws under the build plate.
M118 E1 You should adjust the screws until the sheet of paper slides
M118 E1 under the nozzle with a slight resistance. If the nozzles are
M118 E1 giving different resistance, focus on the right nozzle.
M117 Grab a paper sheet
M300 S880 P50
G4 P50
M300 S880 P50
G4 S1
M117 for leveling
G4 S1
M117 Grab a paper sheet
G4 S1
M117 for leveling
G4 S1
M300 S880 P150
G4 S1
M0 Click to continue

; Point 1
M117 Moving to 1/3
G0 Z10 F1500
G0 X115 Y9 F1000
G0 Z0 F1500
M118 E1 Adjust the front knob until the sheet of paper slides under the
M118 E1 nozzle with a slight resistance, then press the OK button on the
M118 E1 printer.
M300 S880 P50
G4 P50
M300 S880 P50
M0 Adjust front knob

; Point 2
M117 Moving to 2/3
G0 Z10 F1500
G0 X165 Y141 F1000
G0 Z0 F1500
M118 E1 Now, adjust the back-right knob the same way and then press OK.
M300 S880 P50
G4 P50
M300 S880 P50
M0 Adjust right knob

; Point 3
M117 Moving to 3/3
G0 Z10 F1500
G0 X65 Y141 F1000
G0 Z0 F1500
M118 E1 Finally, adjust the back-left knob and press OK.
M300 S880 P50
G4 P50
M300 S880 P50
M0 Adjust left knob

; Confirm results
M117 Centering...
G0 Z10 F1500
G0 X115 Y75 F1000
G0 Z0 F1500
M118 E1 Now that you've adjusted all of the knobs, it's time to confirm
M118 E1 the results. Slide the piece of paper underneath the nozzles
M118 E1 and see if there is slight resistance. If there is too much or
M118 E1 too little resistance, try leveling your bed again.
M117 Check results
M300 S880 P50
G4 P50
M300 S880 P50
G4 P50
M300 S880 P150
G4 S1
M117 Check results
G4 S2
M0 Click to finish
