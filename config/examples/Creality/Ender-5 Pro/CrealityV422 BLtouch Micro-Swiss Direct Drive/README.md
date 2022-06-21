# Configuration files for Stock Ender 5 Pro 4.2.2 Board

This configuration has some tweaks to jerk and acceleration. If you don't want those changes then set these values in the `Configuration.h` file for the following commands.

- Line 1062: `#define DEFAULT_XJERK 10.0`
- Line 1063: `#define DEFAULT_YJERK 10.0`
- Line 1033: `#define DEFAULT_MAX_ACCELERATION      { 500, 500, 100, 10000 }`

It also has z-offset preconfigured at -1.45 which works well for a glass bed with the magnet removed. If you want to define your own offset or you don't want the offset configured in the firmware then change line 1279 to `#define NOZZLE_TO_PROBE_OFFSET { -40, -13, 0 }``

## Direct Drive

If you aren't using a direct drive, then change line 1013 in `Configuration.h` from 

this

`#define DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 800, 137.6 }`

to this

`#define DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 800, 93 }`

## Notice

If you are upgrading from the stock Creality firmware that either came with your printer or off of their website then you will notice the plate seems fliped. The reality is that the plate was flipped on the stock firmware and the Marlin update fixes that. You have probably noticed before that your prints came out oriented differently than what you saw in Cura. No longer! But this will cause your default Cura start code to behave differently than you are used to. You can change this start code

```
G1 X10.1 Y20 Z0.28 F5000.0 ;Move to start position
G1 X10.1 Y200.0 Z0.28 F1500.0 E15 ;Draw the first line
G1 X10.4 Y200.0 Z0.28 F5000.0 ;Move to side a little
G1 X10.4 Y20 Z0.28 F1500.0 E30 ;Draw the second line
```

to this

```
G1 X210.1 Y20 Z0.28 F5000.0 ;Move to start position
G1 X210.1 Y200.0 Z0.28 F1500.0 E15 ;Draw the first line
G1 X210.4 Y200.0 Z0.28 F5000.0 ;Move to side a little
G1 X210.4 Y20 Z0.28 F1500.0 E30 ;Draw the second line
```

and this end code 

`G1 X0 Y0 ;Present print`

to this

`G1 X200 Y200 ;Present print`

and that will cause your printer to behave as it used to. You can get to the start/end code by clicking your printer name in the Prepare tab of Cura and then clicking Machine Settings. 
