# Anycubic I3 Mega – 32-Bit Variant (Trigorilla Pro)

## Usage
Use these configurations like any other configs. Set `default_envs = trigorilla_pro` in `platformio.ini` for a simplified build. Flashing with PlatformIO may be broken. If so you can use OctoPrint firmware flasher plugin or the `stm32flash` tool in the terminal, like so:
```sh
stm32flash -w firmware.bin -v -g 0x0 -b 115200 <YOUR COM/SERIAL PORT HERE>
```

Remove Jumper JP1 from the board to access the bootloader and flash firmware. You can also set SW1 to USB to power the STM32 solely through USB, otherwise the PSU needs to be on to flash. (If you need to flash often it may be worth soldering a button that has a normally closed pin to a BEC plug, and plug that into JP1 instead of the Jumper. That switch can be routed to the outside of the case and held down at boot to enable flashing mode.)

## Features
- Touch screen with Marlin touch menu
- Model Predictive temperature Control for stable hotend temperatures (tune with `M306 T`)
- PID hotend baseline tune included
- PID bed heating
- SD Card
- Filament runout sensor
- Babystepping for realtime first layer adjustments
- Pre-tuned Linear Advance (high at 0.8, reduce to 0.6 if you see underextrusion)
- Power Loss Recovery
- Support for BLTouch (ABL) or manual leveling (UBL)
- Support for TMC2208

## Potential Issues
The Trigorilla Pro board has many issues and anomalies that have not been acknowledged by Anycubic, such as:
- Unstable Vref causes very noisy (+-6°C) extruder temperature measurements. This may be exacerbated by plugging in an SD Card.
- A weak Power Supply may drop the voltage on bed heating, causing Vref to jump and temperature measurements to deviate.
- A Ground Loop with the case severely increases Vref noise.

Fixes:
- Use [plastic mounting](https://www.printables.com/model/188956-m3-nuts-washer-and-bolts) to isolate the board from the case.
- Print over Serial instead of SD Card.
- Ground the frame to earth or neutral.

## Credits
This project would not have been possible without the Marlin Discord and their many helpful members. I would like to thank especially The-EG, EvilGremlin, tombrazier, Dust, and Nuck-TH. Additionally [this](https://www.thingiverse.com/thing:5159397/comments) unfinished firmware from Thingiverse user Thr333DDD is what I formerly based these configs on. [This analysis and reverse engineering](https://github.com/napyk/trigorilla-pro) of the Trigorilla Pro board by Github user napyk was also very helpful in figuring out issues.
