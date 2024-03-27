# Rolohaun Rook MK1 by LDO Motors

The [Rook MK1 by Rolohaun](https://www.printables.com/model/387431-rook-mk1-3d-printer) is meant to be built out of parts you have laying around, but vendors like LDO Motors have put a kit together to simplify the build process. This config is meant for the following hardware:

## Motherboard

* BigTreeTech SKR Mini E3 V3.0

## Motors

> [!IMPORTANT]
> A & B (X & Y) motor currents are set to higher than normal values due to the specific model of motors used. Motor current & sensorless homing values will need to be tuned for your specific hardware.

* A & B motors: LDO-42STH48-2504MAC(F) 0.9°
* Z motor: LDO-42STH40-1684AC 1.8°
* E motor: LDO-42STH25-1004AC 1.8°

## Hotend

 * Trianglelab TCHC TR6

## Extruder

 * Trianglelab DDB Extruder (BMG)

## LCD

* BigTreeTech TFT35

## Fans

> [!NOTE]
> * Hotend cooling fan is connected to `PC7` (`FAN1` header)
>
> * Part cooling fans are connected via Y-splitter to `PC6` (`FAN0` header).
