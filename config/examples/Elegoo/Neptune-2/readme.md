# Elegoo Neptune 2/Neptune 2S Configuration

The example provided has a few custom switches to simplify configuration in the `// @section custom` section of the `Configuration.h` file. The ZNP Robin Nano 1.2 and 1.3 Boards are both supported with only minot changes in `// @section custom` and a `default_envs` change in the `platformio.ini` file.

## For ZNP Robin Nano 1.2 boards:
  - in the `Configuration.h` file, ensure `#define IS_BOARD_1_2` *IS NOT* commented out.
  - Update/Ensure `default_envs = mks_robin_nano35` in the `platformio.ini` file.

## For ZNP Robin Nano 1.3 boards:
  - In the `Configuration.h` file ensure `#define IS_BOARD_1_2` *IS* commented out.
  - In the `platformio.ini` file update/ensure `default_envs = mks_robin_nano_v1_3_f4`.

## TO enable BlTouch (All boards):
  - In the `Configuration.h` file ensure `#define HAS_BLTOUCH` *IS NOT* commented out.
