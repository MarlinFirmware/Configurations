### Malyan M200 Build Instructions

These instructions cover building Malyan M200 firmware with PlatformIO or the Arduino IDE. The example configuration in this folder is for the **M200 V1** (`BOARD_MALYAN_M200`, STM32F103CB). PlatformIO is the recommended way to build it.

> [!WARNING]
> A successful build does not confirm that the firmware works on your printer. Confirm your board revision before flashing. Boards that look like a V1 (no fan at the rear of the base) have turned out to be V2 boards. A build for the wrong MCU will not work, and V2 boards have been reported to boot-loop; see [MarlinFirmware/Marlin#23716](https://github.com/MarlinFirmware/Marlin/issues/23716).

### PlatformIO (M200 V1)

1. Download matching versions of Marlin and these example configurations (use the `bugfix-2.1.x` or release configurations, not `import-2.1.x`). Copy `Configuration.h` and `Configuration_adv.h` to the `Marlin` directory in the Marlin source tree.
2. With PlatformIO installed, run `pio run -e STM32F103CB_malyan` from the root of the Marlin source tree.
3. The firmware binary is `.pio/build/STM32F103CB_malyan/firmware.bin`. Flash it from an SD card:
   - Copy `firmware.bin` to the SD card under three names: `firmware.bin`, `update.bin`, and `fcupdate.flg`. Use the SD card that came with the printer if possible. The bootloader is very picky about SD cards.
   - Follow steps 16-19 of the Arduino IDE instructions below (center the X and Y axes, power-cycle, remove the card and delete `fcupdate.flg`, then test).

### M200 V2 / V3

The later-run V2 and the V3 use an STM32F070 MCU and are not covered by this example configuration. The PlatformIO environments for them are `STM32F070RB_malyan` and `STM32F070CB_malyan` (with `MOTHERBOARD` set to `BOARD_MALYAN_M200_V2`). Only changing `MOTHERBOARD` in this example does **not** produce a working build: the `STM32F070CB_malyan` build overflows the flash by several KB and the `STM32F070RB_malyan` build stops with a `static_assert` error. A V2 or V3 needs a configuration trimmed to fit, along with its own steps-per-mm and axis directions (see steps 11-12 below). The V3 pinout is not complete.

### Arduino IDE

> [!NOTE]
> Building with the Arduino IDE is currently not working. With STM32 Cores 1.9.0 the build stops because `F_CPU` is not a constant expression (see [Configurations#900](https://github.com/MarlinFirmware/Configurations/issues/900)), and STM32 Cores 2.4.0 builds but overshoots the flash size. Adding `#define F_CPU` to the configuration is not a fix, as it breaks PlatformIO builds. Use PlatformIO instead. The steps below are kept for reference.

1. Install the Arduino IDE from your favorite source (arduino.cc, windows store, app store)
2. Launch the IDE to add the ST boards manager:
   - Open the **Preferences** dialog.
   - Add this link in the "*Additional Boards Managers URLs*" field:
      https://github.com/stm32duino/BoardManagerFiles/raw/main/package_stmicroelectronics_index.json
   - Select "**Show verbose ouptut during: compilation**."
3. Select **Tools** > **Board** > **Boards Manager**.
4. Type "Malyan" into the Search field.
5. The board package is "**STM32 Cores by STMicroelectronics**." Choose install. This will download many tools and packages, be patient.
6. Open the **Tools** > **Board** submenu, scroll all the way down, and select **3D Printer Boards**.
7. From the **Tools** menu, select a board part number:
   - If you own a M200 V1 or early run (black V2), choose **Malyan M200 V1**.
   - If you own a M200 V2 later run (white/black) or V3 (Pro), choose **Malyan M200 V2** (The V2 and V3 both share an STM32F070 MCU). Note that the V3 pinout is not complete (autolevel doesn't work as of this writing).
8. From the **Tools** menu, choose **USB Support** > **CDC No Generic Serial**.
9. Download the [latest Marlin source](//marlinfw.org/meta/download/) and unzip it.
10. Look in the `Marlin` subdirectory for the `Configuration.h` and `Configuration_adv.h` files. Replace these files with the configurations in the `config\examples\Malyan\M200` folder.
11. If you have an early-run V2, the steps-per-mm are roughly half. Consult the [mpminipro.com wiki](//mpminipro.com/) for the steps that apply to your unit. Modify `Configuration.h`.
12. Inverting Axis. There's no pattern to axes will need to be inverted. The only way to know is to test your particular printer. If you *do* know, go ahead and invert the correct axes.
13. Open the `Marlin/Marlin.ino` file in Arduino IDE.
14. From the **Sketch** menu, select **File** > **Export Compiled Binary**.
15. When compilation is done you've built the firmware. The next stage is to flash it to the board. To do this look for a line like this: `"path/to/bin/arm-none-eabi-objcopy" -O binary "/path/to/Marlin.ino.elf" "/path/to/Marlin.ino.bin"`
  The file `Marlin.ino.bin` is your firmware binary. M200 (v1-3) and M300 printers require flashing via SD card. Use the SD card that came with the printer if possible. The bootloader is very picky about SD cards. Copy `Marlin.ino.bin` to your SD card under three names: `firmware.bin`, `update.bin`, and `fcupdate.flg`.
16. Insert the SD card into your printer. Make sure the X and Y axes are centered in the middle of the bed. (When X and Y endstops are closed this signals a UI upgrade to the bootloader.)
17. Power-cycle the printer. The first flash may take longer. Don't be surprised if the .99 version number doesn't show up until after the UI has launched the default screen.
18. Remove the SD card and delete the `fcupdate.flg` file from the card to prevent an accidental re-flash.
19. Test the endstops and homing directions, run M303 PID autotune, and verify all features are working correctly.

Welcome to Marlin 2.x...
