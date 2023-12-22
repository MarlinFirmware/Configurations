# Display firmware, boot image and icons compilations

Some features, such as G-code preview, need updated firmware to work on some DACAI and TJC displays. Custom icon assets such as Giadej icon set are only supported by DWIN and DACAI displays.

If you have the stock icon set, in principle you **do not need to update the display to use this firmware**, only some TJC display units need a firmware update to boot properly. Creality currently provides several types of display units with its Ender-3 V2/S1/Neo printers:

## LCD Display Firmware Update
In order to use all the features of ProUI, display screens must be updated.
If you can't see preview images with this [g-code test file](../slicer%20scripts/cura/SimpleCuraTest.gcode) update your screen firmware.

**DWIN display**, the original display unit, it supports all firmware functions.  
[![Ender3v2-DWIN](https://user-images.githubusercontent.com/2745567/156829365-a58a3afc-77e3-40b9-9e16-5edfe3073de8.jpg)](https://raw.githubusercontent.com/MarlinFirmware/Marlin/bugfix-2.1.x/display%20assets/displays/DWIN.jpg)

**DACAI display**, some versions need updated firmware to enable G-code preview.  
[![Ender3S1-DACAI](https://user-images.githubusercontent.com/2745567/156829472-2c38a4ab-bdde-4c21-b78f-a30692c96500.jpg)](https://raw.githubusercontent.com/MarlinFirmware/Marlin/bugfix-2.1.x/display%20assets/displays/DACAI.jpg)

**SYNWIT (VIEWE) display**, initially unsupported due to incompatibilities with QR-codes (removed in latest firmware version) some users [report problems](https://github.com/MRiscoC/Ender3V2S1/issues/323) with this screen, but now seems that it is working without issues.  
[![VIEWE](https://user-images.githubusercontent.com/2745567/163235004-1d3f1ed4-e149-4ca8-ae60-438df5f0b70a.png)](https://raw.githubusercontent.com/MarlinFirmware/Marlin/bugfix-2.1.x/display%20assets/displays/SYNWIT1.jpg)
[![SYNWIT2R](https://user-images.githubusercontent.com/2745567/209407402-25053f01-6a5d-4c76-90c8-da5aec43100c.png)](https://raw.githubusercontent.com/MarlinFirmware/Marlin/bugfix-2.1.x/display%20assets/displays/SYNWIT2.jpg)

**TJC display**, currently this display needs a _special compile_ to show leveling numeric data in the mesh viewer and some displays need updated firmware to enable G-code preview and boot properly,
more info: [TJC issues](https://github.com/MRiscoC/Ender3V2S1/issues/542).  
[![TJC](https://user-images.githubusercontent.com/2745567/206931166-24185525-e377-472e-9bed-37a39aab24fb.jpg)](https://raw.githubusercontent.com/MarlinFirmware/Marlin/bugfix-2.1.x/display%20assets/displays/TJC.jpg)

The `DWIN_SET` display firmware / icon assets only apply to the DWIN display, for the DACAI screens, you should use the `private` display firmware / icon assets.

# Display firmware, boot image and icons compilations
The display assets compilations in this page are compatible with ProUI - Professional firmware. Each firmware can have its own compatible icon set.

## How to install
1. Get a Micro SD card of 8GB or less.
1. Format the SD card to FAT32 with a 4k/4096 sector allocation size
1. Copy the `DWIN_SET`(DWIN), `private`(DACAI) or `TJC_SET` (TJC) folder in the Root of SD
1. Turn off your printer
1. Disconnect and disassemble the screen unit
1. Install the SD card into the slot of the screen unit
1. Reconnect the screen to the printer
1. Turn on the printer and wait for the display to change color from blue to red/orange
1. Verify that the screen assets were updated
1. Turn off the printer and remove the SD card from the screen unit
1. Reassemble the screen unit

Be sure to leave **only** the `DWIN_SET` or `firmware.zlib` and `private` folder at the root of the card.

If you weren't able to update the display, verify the format of the SD Card
(MBR, FAT32 and allocation unit of 4096 bytes) and the CRC of the files.

If icons are missing after the update, you may need to rename the `.ICO` file. If `USE_STOCK_DWIN_SET` is disabled in Marlin configurations, it uses `7.ICO`, otherwise it uses `9.ICO`.

---

## Using a Custom Display Set

### [Voxelab](Voxelab)

<a href=Voxelab><img src="https://github.com/classicrocker883/MRiscoCProUI/assets/18502096/30ed1822-e5d5-4be5-9283-636390933178" height="400" /></a>

<br>

- Copy one of the `DWIN_SET`s from [Voxelab/DWIN Sets](Voxelab/DWIN%20Sets) to a Micro SD card. Remove the identifier so the folder is just named `DWIN_SET`.  
(i.e. `DWIN_SET (Custom)` => `DWIN_SET`)
- Follow the instructions on [How to install](https://github.com/MarlinFirmware/Configurations/tree/HEAD/config/examples/Creality/Ender-3%20V2/LCD%20Files/Custom%20Display%20Sets/README.md#how-to-install).

---

### [Creality](Creality)

<a href=Creality><img src="https://raw.githubusercontent.com/mriscoc/Ender3V2S1/Ender3V2S1-Released/screenshots/main.jpg" height="400" /></a>

<br>

### [Giadej](Giadej)

<a href=Giadej><img src="https://raw.githubusercontent.com/mriscoc/Ender3V2S1/Ender3V2S1-Released/display%20assets/Giadej%20compilation/preview1.jpg"  height="400" /></a>

<br>

- For DWIN Display
- - Copy the `DWIN_SET` folder to a Micro SD card.
- For DACAI Display
- - Copy `firmware.zlib` and `private` folder to a Micro SD card.
- Follow the instructions on [How to install](https://github.com/MarlinFirmware/Configurations/tree/HEAD/config/examples/Creality/Ender-3%20V2/LCD%20Files/Custom%20Display%20Sets/README.md#how-to-install).


---

### Credits
- [**Creality**](https://github.com/CrealityOfficial) | [creality.com/download](https://www.creality.com/download)
- [**Voxelab**](https://github.com/Voxelab-64) | [voxelab3dp.com/download](https://www.voxelab3dp.com/download)
- [**alexqzd**](https://github.com/alexqzd) for editing and making icons available
- [**MRiscoC**](https://github.com/mriscoc) for wiki and display files
- [**Giadej**](https://github.com/Giadej) for other icons and custom Boot-Screen
- [**Lighty1989**](https://github.com/Lighty1989) for "XYZ Move Axis" icons and "Bed Points" icons
- [**Gothcha**](https://github.com/gothcha) for other icons
- [**ClassicRocker883**](https://github.com/classicrocker883) for updating the icons

### DWIN_SET CRC
|  Firmware Set        |File                        | SHA-256
|----------------------|----------------------------|-----------------------
|                      |T5UIC1.CFG                  | E1C573639BFA2B3A06C2FA7AD3CAB483653DD3DC383217FF653FAB3145458095
|                      |T5UIC1_V20_4??_191022.BIN   | F8F9A3075AE5516328044ACB79CA522753133B66F1ECBD108E7B5DB2F3FF2FE5
|                      |0T5UIC1.HZK                 | 27F3AE70117DC031E6EA542654CA03B89BB9A0592B23AA9B7E452C35583C0108
|Creality              |9.ICO                       | 2F00B9355034C9DF2819DB56CA5F46C5015071DB5D380AABA3BB10FE3F1A63D2
|Giadej                |9.ICO                       | 47939E140DE3E55F7BEDFBDC70068C228A8BDE0E72BE673635ED216311A6E5C5
|Custom                |9.ICO                       | 6BF0CFF10D61DE64D98BF286B0B60EE91FA88B0CA7FC7AF777CB6C9C71F15F1C
|Gotcha                |9.ICO                       | D90B25EE7675E61FFA8E8CD1B4E9435DFD4A51FADC767D291B50064C005AA8B4
|Original              |9.ICO                       | B19C67B762B6A29DC1D7BE5E2A5EDCD58E31EC40BC28125A2F361986BE019000
|Voxelab Original Light|9.ICO                       | 9C6274182E39E2D1A2FEC8C907C10F9590AFD16ABEB4027B2ADB560A642FBB8A
|Voxelab Red           |9.ICO                       | E2FB515545AFF7AE8C4AD794CDAEFA4E1A8B5E9E84A3CAD6B04898F68ECDD5B5
