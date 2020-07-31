# Notes
- At this time, this version is not supported by the stock bootloader as an SD card update.
- Special thanks to Korbinian Heel [[@inib](https://github.com/inib)]
- Special thanks to Slava Novgorodov [[@Slava N](https://www.youtube.com/channel/UC617QlzItK-dOeTTttKZq3A)] for sharing and making the video of the direct installation method
- Special thanks to Sebastian Hernandez [[@SXHXC](https://github.com/SXHXC)] for his [fork](https://github.com/SXHXC/Marlin-Anycubic-Predator-Trigorilla-PRO) and doing all the work

# Flash & Restore
## Steps to build, prepare and flash the board
 1. Use these example config files, adjust to your needs and build Marlin
 2. **Turn off and disconnect AC power**
 3. Move the jumper **SW1** to **USB** and **remove JP1 jumper** ![welded cables](/Images/JUMPERS.png)
    - **JP1** It is connected to the pin BOOT0, which blocks the programming, it should be removed.
    - **SW1** Power the board from the USB port or from the external 24V source, for security purposes change this position at least while doing the programming.
 4. Download [STM32 Flasher](https://www.st.com/en/development-tools/flasher-stm32.html#get-software) 
 5. See this video:  
 [![Trigorilla Pro reflash to Marlin 2.0.x](https://img.youtube.com/vi/g2cAJXle6t0/0.jpg)](https://www.youtube.com/watch?v=g2cAJXle6t0 "ANYCUBIC Predator original board Trigorilla Pro reflash to Marlin 2.0.x")    
 6. Restores all jumpers to their original position
 7. Finished!
 
## Backup and restore.
 - If you made the backup as described in the video just flash this file instead of the Marlin binary.