# Troubleshooting tips for Proforge 2s Dual

## Servomotor switch overheating?
```cpp
// Only power servos during movement, otherwise leave off to prevent jitter
#define DEACTIVATE_SERVOS_AFTER_MOVE
```

## Don't forget to Tune PID with `M303`

- Enable `EEPROM_SETTINGS` so tuned PID values can persist after reboot.
- Enable `PIDTEMPBED` to enable PID tuning for the bed.

```cpp
#define PID_DEBUG             // Print PID debug data to the serial port. Use 'M303 D' to toggle activation.
#define PID_PARAMS_PER_HOTEND // Use separate PID parameters for each extruder (useful for mismatched extruders)
```
