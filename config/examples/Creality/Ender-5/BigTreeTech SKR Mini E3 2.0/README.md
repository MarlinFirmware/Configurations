# Ender-5 with BigTreeTech SKR Mini E3 v2.0

## Older Leadscrew

> [!NOTE]
> This Ender-5 `Configuration.h` applies to the newer leadscrew with 800 steps/mm. If your printer has the older leadscrew, change the Z component of `DEFAULT_AXIS_STEP_PER_UNIT` to 400 as in the example below:

```cpp
#define DEFAULT_AXIS_STEPS_PER_UNIT { 80, 80, 400, 93 }
```
