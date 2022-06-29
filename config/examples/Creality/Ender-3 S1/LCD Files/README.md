# Ender 3 S1

# Display firmware, boot image and icons compilations

Currently Creality provides two kinds of screen units:

**Original Ender 3V2 DWIN display**  
![Ender3v2-DWIN](https://user-images.githubusercontent.com/2745567/156829365-a58a3afc-77e3-40b9-9e16-5edfe3073de8.jpg)

**Original Ender 3S1 DACAI display**  
![Ender3S1-DACAI](https://user-images.githubusercontent.com/2745567/156829472-2c38a4ab-bdde-4c21-b78f-a30692c96500.jpg)

For the Ender 3S1 you must to use the `private` display firmware / icon assets, available here: `../config/examples/Creality/Ender-3 V2/LCD Files`

## How to install
1. Get an SD card of 8GB or less.
1. Format the SD card MBR, FAT32 and with a 4 KB sector size
1. Copy the `private` directory in the Root of SD
1. Turn off your printer
1. Disconnect and disassembly the screen unit
1. Install the SD card into the internal slot of the screen unit
1. Reconnect the screen to the printer
1. Turn on the printer and wait for the display to complete all tasks, confirming the procedure success, with the progress bar at 100%
1. Turn off the printer and remove the SD card from the screen unit
1. Reassembly the screen unit 
1. Turn on the printer and verify that the screen assets were updated
  
If you want to change only the icons, then you can leave only the **9.ICO** file inside of the DWIN_SET folder.  
If you weren't able to update the display, verify the format of the SD Card (MBR, FAT32 and allocation unit of 4096 bytes) and the CRC of the files.
  
Be sure to leave **only** the `private` folder at the root of the card.  
  
---

In: https://github.com/mriscoc/Ender3V2S1/blob/Ender3V2S1-Released/display%20assets/readme.md
