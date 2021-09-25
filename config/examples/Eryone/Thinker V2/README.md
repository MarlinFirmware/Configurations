## Eryone Thinker V2

 - BLTouch probe
 - Filament runout Sensor

## How to use the config
#### Check the hardware of your printer
 1. You are using the stock printer, no need to modify the config
 2. You are using the Filament runout sensor:
    Enable this line(Delete the "//" to enable it)
    - //#define THINKERV2_FL  //Enable for an installed Filament runout sensor
 3. You are using the Bltouch:
    Enable this line(Delete the "//" to enable it)
    - //#define THINKERV2_BLTOUCH  // Enable for an installed BLTOUCH
 4. You are using the direct drive extruder:
    Enable this line(Delete the "//" to enable it)
    - //#define THINKERV2_Direct //Enable for Direct drive extruder system
 5. Can I use all of the mod? The answer is yes. You can use all of them or just a part of them.
 6. If your printer PSU has a reset problem. You can disable the PIDTEMPBED feature
    Disable this line(Add the "//" to disable it)
    - #define PIDTEMPBED  // If your PSU has a reset problem then try to disable it to improve this problem

## Have fun :)
