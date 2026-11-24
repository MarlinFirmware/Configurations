# PancakeBot

Configuration for the [PancakeBot](https://www.pancakebot.com) batter-dispensing plotter.

- Board: PancakeBot (RAMPS 1.3 based), `BOARD_RAMPS_PANCAKEBOT`.
- X and Y axes only (Z is disabled). There is no extruder or heater.
- `M106` / `M107` switch the batter pump, which stops while a print is paused.
- Front panel: `PANCAKEBOT_PANEL` with a 128x32 display, Up / Down / Select / Back buttons, and LEDs for SD printing and SD errors.
- The Marlin boot screen and the progress text options are disabled because they don't fit the 128x32 display. The status screen has a progress bar.
