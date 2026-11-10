## Elegoo Neptune 3 Plus Configuration

> [!IMPORTANT]
> The firmware binary file must be named `ZNP_ROBIN_NANO.bin` or it will not flash.

- Mainboard: ZNP Robin Nano_DW V2.2 (`BOARD_MKS_E3D_V2`, STM32F401RC with a 32KiB bootloader).
- `platformio.ini`: Set `default_envs` to `mks_e3d_v2`. The build names the binary `ZNP_ROBIN_NANO.bin`.
- Copy the binary to an SD card formatted as FAT32 and power on the printer with the card inserted.

The stock TJC touch screen is supported with `ELEGOO_NEPTUNE_3_TFT` and works with the screen's original firmware; it does not need to be reflashed.
