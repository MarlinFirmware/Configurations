## Elegoo Neptune 2/Neptune 2D/Neptune 2S Configuration

***IMPORTANT:*** The firmware binary file must be named `elegoo.bin` or it will not flash.

The provided configuration includes custom switches at the top of `Configuration.h` to simplify the build options. It supports both the ZNP Robin Nano 1.2 and 1.3 Boards with only minor configuration changes. By default, the configuration applies to the 1.3 board without BLTouch.

NOTE: The original Neptune 2 and 2S use the same configurations, but the 2S always uses the 1.3 version of the board.

### ZNP Robin Nano 1.2 boards:
- `Configuration.h`: Disable `IS_BOARD_1_3`.
- `platformio.ini`: Set `default_envs` to `mks_robin_nano_v1_2`.

### ZNP Robin Nano 1.3 boards:
- `Configuration.h`: Enable `IS_BOARD_1_3`.
- `platformio.ini`: Set `default_envs` to `mks_robin_nano_v1_3_f4`.

### BLTouch (all boards):
- `Configuration.h`: Enable `HAS_BLTOUCH`.

### Neptune 2D (All boards):
- `Configuration.h`: Enable `IS_2D`.
