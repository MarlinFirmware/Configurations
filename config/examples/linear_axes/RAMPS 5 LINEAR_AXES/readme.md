## Simple example for using a RAMPS with 5 linear axes and 0 extruders.

The axis are X,Y,Z,U and V

All axis are set the same with identical steps/mm, acceleration etc

Internally the aditional axes are always I, J and K (K is not used in thie example)
These are then mapped to external axis names with AXIS4_NAME, AXIS5_NAME and AXIS6_NAME defines.

In this example I and J axis automaticly use the E0 and E1 pins since as there is no extruder.

NB You do have to manualy set the endstop pins.
I have set the endstops as I_STOP_PIN 65 and J_STOP_PIN 66 both on AUX-2
