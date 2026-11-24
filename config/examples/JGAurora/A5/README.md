# Configuration for JGAurora A5 printer

> [!IMPORTANT]
> Before flashing your printer, unplug the 8-pin LCD panel header connector. The LCD should turn off completely. This is found underneath the LCD, and can be accessed from underneath the printer without removing any screws. Remember where it goes so you can put it back after flashing.

## Graphical Display

The control panel included with the JGAurora interfaces only indirectly with Marlin, and this imposes some limitations. But you can use a RepRap Discount Full Graphic Smart Controller with the JGAurora A5 by applying the following additional settings in `Configuration.h`:

```cpp
#define ENCODER_PULSES_PER_STEP 5
#define ENCODER_STEPS_PER_MENU_ITEM 1
#define REVERSE_ENCODER_DIRECTION
#define REPRAP_DISCOUNT_FULL_GRAPHIC_SMART_CONTROLLER
```

You may also be able to change `BEEPER_PIN` to use the piezo on the LCD controller instead of the one on the board.
