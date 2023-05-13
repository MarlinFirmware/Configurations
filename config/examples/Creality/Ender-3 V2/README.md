# Display update guide for Ender-3 V2 family screens

This guide applies for all Ender-3 series printers that use a **color LCD with rotary encoder**.

Screen updates are handled via a microSD card. In order to update, the display module needs to be opened to reveal the mainboard.

## **Identifying your display type**

Currently, Creality provides screen units from four different manufacturers.

The communication between the printer and display is more or less the same (with some slight compatibility quirks), but the format of the firmware and/or graphics assets differs.

Use the following pictures to identify your type of display unit:

* **DWIN display**, originally shipped with Ender-3 V2

    ![Ender3v2-DWIN](https://user-images.githubusercontent.com/2745567/156829365-a58a3afc-77e3-40b9-9e16-5edfe3073de8.jpg)

* **DACAI display**, a DWIN clone

    ![Ender3S1-DACAI](https://user-images.githubusercontent.com/2745567/156829472-2c38a4ab-bdde-4c21-b78f-a30692c96500.jpg)

    Emulates the DWIN protocol but without:
    * Proper brightness control
        * Display brightness seems to have a non-linear curve, only dimming under `50` out of `255`
    * Display rotation
        * This makes it incompatible with MarlinUI in Landscape mode

    Renders TrueType fonts instead of Bitmap fonts.

    DACAI tools allow for the conversion of original `DWIN_SET` asset bundles into its own format.

* **SYNWIT / VIEWE display** **`Currently undocumented`**, **`Reduced custom UI compatibility`**

    ![Ender3V2S1-SYNWIT-VIEWE](https://user-images.githubusercontent.com/2745567/209407402-25053f01-6a5d-4c76-90c8-da5aec43100c.png)

    Emulates the DWIN protocol, but without:
    * Direct pixel blitting
        * This makes it incompatible with `gcode`-based STL previews

    There is currently no information regarding how to compile a firmware for this type of display, nor does it look like there are any official firmwares to attempt a decompilation effort.

* **TJC display** **`Currently undocumented`**, **`Currently incompatible with custom UIs`**

    ![Ender3V2S1-TJC](https://user-images.githubusercontent.com/2745567/206931166-24185525-e377-472e-9bed-37a39aab24fb.jpg)

    Appears to emulate the DWIN protocol but without an unknown subset of features that make it currently crash with custom firmware.

    TJC tools are readily available, but there are currently no custom display firmwares for this unit. More research is required, but it appears custom firmware should be possible.

## **Display compatibility**

The differences between the types of displays units shown above make them more compatible or less compatible with different types of UIs:

* **DWIN**
    * ✅ Creality UI
    * ✅ MRiscoC Pro UI
    * ✅ JyersUI
    * ✅ MarlinUI Portrait
    * ✅ MarlinUI Landscape
* **DACAI**
    * ✅ Creality UI
    * ✅ MRiscoC Pro UI
    * ✅ JyersUI
    * ✅ MarlinUI Portrait
    * ❌ MarlinUI Landscape
        * Lack of support for display rotation
* **SYNWIT / VIEWE**
    * ✅ Creality UI
    * ⚠️ MRiscoC Pro UI
        * STL preview not working
    * ❔ JyersUI
    * ⚠️ MarlinUI Portrait
        * Lack of custom graphics assets compilation means no icons are visible
    * ❔ MarlinUI Landscape
* **TJC**
    * ✅ Creality UI
    * ❌ MRiscoC Pro UI
        * As reported by author; incompatibility causes currently unknown
    * ❔ JyersUI
    * ⚠️ MarlinUI Portrait
        * Lack of custom graphics assets compilation means no icons are visible
    * ❔ MarlinUI Landscape

## **If you've got a currently undocumented display**

In the case of **SYNWIT / VIEWE** and **TJC** displays, currently only the Creality UI interface option (`DWIN_CREALITY_LCD`) is fully compatible.

If you have a **DWIN** or **DACAI** display, please follow the procedure below to upgrade the firmware with the custom graphics assets required for MRiscoC Pro UI, JyersUI and MarlinUI.

(It is worth noting that MarlinUI _will_ work on undocumented LCDs, but no icons will be displayed).

## **Updating the Display**

* ### `DWIN` units
    - Format a microSD card using the FAT32 filesystem with 4K cluster size
    - Copy the `DWIN_SET` folder to the SD card and insert the card into the slot on the back of the display unit.
    - Power on the machine and wait for the screen to change from blue to orange
    - Power off the machine
    - Remove the SD card from the back of the display
    - Power on to confirm a successful flash
* ### `DACAI` units
    - Format a microSD card using the FAT32 filesystem with 4K cluster size
    - Copy the `private` folder to the SD card and insert the card into the slot on the back of the display unit.
    - Power on the machine and wait for the installation screen to finish
    - Power off the machine
    - Remove the SD card from the back of the display
    - Power on to confirm a successful flash

If you're experiencing screen glitches, please ensure both the printer and the display unit have been flashed correctly.
