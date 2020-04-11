# Flying bear P905H configuration for Marlin Firmware

This configuration was tested on **single extruder P905H with inductive Z-sensor**.
I've tried to make printer work smoothly.
Thus this configuration focused mostly on print quality than on speed.

You could use this firmware as a baseline for other P905 modifications.
There are some notes in config files you could find them by "P905H" string.

## Build HOW TO
  - Install PlatformIO IDE
  - Download Marlin source code
  - Copy *.h files from this folder to Marlin folder
  - Now you can build and upload firmware using PlatformIO project tasks in **env:mega2560** section
  - Do not forget to reset your default settings right after update