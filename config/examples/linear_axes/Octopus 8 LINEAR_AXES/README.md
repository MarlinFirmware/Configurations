## Octopus with 8 Linear Axes (no extruders)

The axes are controlled with parameters `X`, `Y`, `Z`, `A`, `B`, `C`, `U`, and `V`.

All axes in this example use the same steps/mm, acceleration, etc.

NOTE: Internal to Marlin the first five additional axes are called I, J, K, U and V. However,
the G-code parameters for extra axes are assigned using AXIS4_NAME, AXIS5_NAME, AXIS6_NAME, etc.

In this example Marlin automatically maps extra axes to the unused E0, E1, E2, E3 and E4 (Z2) stepper ports.
Endstop pins must be assigned manually, so this example assigns endstops as follows:

```
I_MIN_PIN PG11  // Z2-STOP
J_MIN_PIN PG12  // E0DET
K_MIN_PIN PG13  // E1DET
U_MIN_PIN PG14  // E2DET
V_MIN_PIN PG15  // E3DET
```
