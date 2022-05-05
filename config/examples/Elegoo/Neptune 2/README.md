# Elegoo Neptune 2/Neptune 2D/Neptune 2S Configuration

*IMPORTANT:* Once compiled, be sure to rename `Robin_nano35.bin` to `elegoo.bin` before flashing.

Compiled binaries of configurations are available here: https://github.com/just-trey/Marlin/tree/elegoo-neptune-2/config/Elegoo/Neptune-2

The configuration provided has custom switches in the `Configuration.h` file `// @section custom` to simplify the build options. This configuration supports the ZNP Robin Nano 1.2 and 1.3 Boards with only minor changes in `// @section custom` and a `default_envs` change in the `platformio.ini` file. The configuration is currently set for the 1.3 board without BLTouch, which is the most common option.

NOTE: The original Neptune 2 and 2S use the same configurations except the 2S is always a 1.3 version of the board.

## For ZNP Robin Nano 1.2 boards:
  - In the `Configuration.h` file, ensure `#define IS_BOARD_1_3` is set to `false`.
  - Update/Ensure `default_envs = mks_robin_nano35` in the `platformio.ini` file.

## For ZNP Robin Nano 1.3 boards:
  - In the `Configuration.h` file, ensure `#define IS_BOARD_1_3` is set to `true`.
  - In the `platformio.ini` file update/ensure `default_envs = mks_robin_nano_v1_3_f4`.

## To enable BlTouch (All boards):
  - In the `Configuration.h` file, ensure `#define HAS_BLTOUCH` is set to `true`.

## For the Neptune 2D (All boards):
  - In the `Configuration.h` file, ensure `#define IS_2D` is set to `true`.
