# Y AXIS HOMING WARNING
If you get premature Y axis endstop triggers or even halts this is a known problem with the BigBox. The Y endstop wiring runs alongside the X motor wiring. Designer Greg Holloway recommends switching this setup to be active high and trigger low. My suggestion is to fix mount the Y axis switch to the frame and run the endstop wire down the front of the frame. 

# Microstepping
The Y axis should be jumpered to 8 microsteps with the stock geared setup with 0.9 degree stepper. 16 microsteps even at low speeds would overrun the RUMBA. 1.8 degree steppers can run 16 microsteps and there would be no change to the steps per mm in this configuration.

# Probe
The configuration is for the original IR probe which has problems with the glass bed. A popular modification was to move this to the bed for Z homing. I switched to a capacitive probe which can be run to the original wiring if you separate the 5v line and move it to a 12v source on the board. Endstop hit state needs to be changed to LOW for this.

# Octoprint
Many of these were delivered with the Octoprint upgrade. When adjusting the config for recommended Octoprint options the following values have been tested to fit within the ram limitations of the RUMBA. There is enough ram leftover to increase one of these settings but not others.
```cpp
BLOCK_BUFFER_SIZE 16
BUFSIZE 8
TX_BUFFER_SIZE 32
RX_BUFFER_SIZE 1024
```

# Purge Bucket
Y max at most X positions is 200. The purge bucket is at 235 starting around X 70. This is configured for nozzle wipe but does not seem usable for parking position due to the 35mm offset between T0 and T1.
