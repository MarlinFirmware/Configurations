### Elegoo Neptune 2/Neptune 2D/Neptune 2S Configuration

***IMPORTANT:*** Once compiled, make sure that file is named `elegoo.bin` before flashing.

The configuration provided has custom switches in the `Configuration.h` file `// @section custom` to simplify the build options. This configuration supports the ZNP Robin Nano 1.2 and 1.3 Boards with only minor changes in `// @section custom` and a `default_envs` change in the `platformio.ini` file. The configuration is currently set for the 1.3 board without BLTouch.

NOTE: The original Neptune 2 and 2S use the same configurations except the 2S is always a 1.3 version of the board.

##### For ZNP Robin Nano 1.2 boards:
  - In the `Configuration.h` file, ensure `#define IS_BOARD_1_3` is commented out.
  - Update/Ensure `default_envs = mks_robin_nano_v1v2` in the `platformio.ini` file.

##### For ZNP Robin Nano 1.3 boards:
  - In the `Configuration.h` file, ensure `#define IS_BOARD_1_3` is uncommented.
  - In the `platformio.ini` file update/ensure `default_envs = mks_robin_nano_v1_3_f4`.

##### To enable BlTouch (All boards):
  - In the `Configuration.h` file, ensure `#define HAS_BLTOUCH` is uncommented.

##### For the Neptune 2D (All boards):
  - In the `Configuration.h` file, ensure `#define IS_2D` is uncommented.
  
  
