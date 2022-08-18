#### How to modify ZNP Nano v1.x board for native USB.

#####Why?
STM32F103/F407 have native USB capabilities, but this board use CH340 USB-serial chip, which greatly limits communication speed (realistucally, no more than 250kbps) and raise the chance of communucation error and missing data. This is most critical in case you use Octoprint or other host software. Native USB-CDC mode communicate at much greater speeds (in our case it'll be around 1.5Mbps) which drastically lowers chance of communication timeout and/or buffer overrruns.

#####How?
1. Cut two traces near CH340 chip (1), two going to endtops (2) and remove two resistors (3) as shown. Scratch off some of the mask from traces on the microcontroller side (2). Optionally you can remove CH340 chip too.

![alt text](/images/1cut.jpg)

2. Solder wires as shown, make new USB wires (under) are exact same length and stick together closely. Use thinnest insulated wires you can (photo show thickest possible). Great choice are wires from laptop screen cable, or good lacqered wire.

![alt text](/images/2wire.jpg)

3. Add 1.5kΩ pullup resistor for D+ signal as shown:

![alt text](/images/3pullup.jpg)

4. Set `default_envs = mks_robin_nano_v1v2_usbmod` or `default_envs = mks_robin_nano_v1_3_f4_usbmod` in platformio.ini, add/uncomment `USB_MOD` in `Configuration.h` and build Marlin.
