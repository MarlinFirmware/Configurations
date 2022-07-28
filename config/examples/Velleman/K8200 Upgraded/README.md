# Updated Example Configuration for Velleman [K8200](http://www.k8200.eu/)

I have taken @CONSULiTAS' excellent configuration file, and added support for the
following:

* VM8204 Z Axis and coupler. This was just a stub previously
* Full Graphic LCD Controller with SD

In addition to the existing options
* VM8201 LCD Controller

I believe the configuration should work for all these options, but since I was
only able to test with the VM8204 and full graphic LCD, I have created a new
configuration. If you don't have an upgraded K8200 or 3drag, you may wish to
use the original version.

# Instructions

If you have a VM8204 upgraded Z axis and coupler, ensure the following line
is uncommented. Otherwise comment it out:

```
#define K8200_K8204
```
If you have the VM8201 display unit, uncomment the following line
```
// #define K8200_VM8201
```

If you have the *3D Printer Full Graphic Smart Controller with 3Drag adapter* (or other screen based on the [RepRap Discount Full Graphic Smart Controller](https://reprap.org/wiki/RepRapDiscount_Full_Graphic_Smart_Controller)), ensure
the following is uncommented, otherwise comment it out
```
#define FULLGRAPHIC_CONTROLLER_LCD_SD
```

## Notes

I (pau1ie) tested this configuration on my K8200 with VM8204 Z axis and
full graphic controller. I purchased a 3drag controller main board which is
identical to the Velleman supplied one, so I am confident this firmware
will also work with the 3drag as CONSULiTAS states below.

Only one LCD screen is supported (they plug into the same place), so only one of them should be uncommented.
 Leaving both controllers uncommented is likely to result in firmware that doesn't work with either.

There is a configuration option for the K8203 Direct Drive Extruder, but
it does nothing at present.

In addition to the firmware sources below, see the following for for genuine [3drag Firmware](https://3dprint.elettronicain.it/blog/2012/09/06/software/)


# Original Readme

* Configuration files for **Vellemann K8200** (with [VM8201](http://www.vellemanprojects.eu/products/view/?id=416158) - LCD Option for K8200)
* K8200 is a 3Drag clone - configuration should work with 3Drag https://reprap.org/wiki/3drag, too. Please report.

* updated manually with parameters from genuine Vellemann Firmware "firmware_k8200_marlinv2" based on the recent development branch

* VM8201 uses "DISPLAY_CHARSET_HD44870 JAPANESE" and "ULTIMAKERCONTROLLER"
* german (de) translation with umlaut is supported now - thanks to @AnHardt for the great hardware based umlaut support

I [@CONSULitAS](https://github.com/CONSULitAS) tested the changes on my K8200 with 20x4-LCD and Arduino 1.6.12 for Mac (SD library added to IDE manually), 2016-11-18 - everything works well.

**Source for genuine [Vellemann Firmware](http://www.k8200.eu/support/downloads/)**
* V2.1.1 (for z axis upgrade, date branched: 2013-06-05): [firmware_k8200_v2.1.1.zip](http://www.k8200.eu/downloads/files/downloads/firmware_k8200_v2.1.1.zip)
  * see also https://github.com/CONSULitAS/Marlin-K8200/tree/Vellemann_firmware_k8200_v2.1.1.zip

* V2 (with LCD/SD-Support, date branched: 2013-06-05): [firmware_k8200_marlinv2.zip](http://www.k8200.eu/downloads/files/downloads/firmware_k8200_marlinv2.zip)
  * see also https://github.com/CONSULitAS/Marlin-K8200/tree/Vellemann_firmware_k8200_marlinv2.zip

* V1 (without LCD/SD-Support, date branched: 2012-10-02): [firmware_k8200_marlinv1.zip](http://www.k8200.eu/downloads/files/downloads/firmware_k8200_marlinv1.zip)
  * see also https://github.com/CONSULitAS/Marlin-K8200/tree/Vellemann_firmware_k8200_marlinv1.zip