# CAN Bus Test: BigTreeTech Octopus Max EZ V1.0

A bench configuration for trying Marlin's CAN bus support (MarlinFirmware/Marlin#28847) with a CAN toolhead board. It is not a printer configuration.

- Board: BigTreeTech Octopus Max EZ V1.0 (STM32H723ZE). CAN port: PD0 (RX) / PD1 (TX), FDCAN1.
- PlatformIO environment: `STM32H723ZE_btt`
- Host connection: USB (`SERIAL_PORT -1`).
- The hotend and bed use the dummy sensor 998 (always 25°C), so the board starts with nothing connected. Don't connect heaters.

## Building

Build the Marlin pull request branch with these files. The two `#error` lines at the top of `Configuration.h` only exist in this staging branch; delete them before building.

## Wiring

- Connect CAN-H to CAN-H and CAN-L to CAN-L, preferably with a twisted pair.
- Terminate the bus with 120 Ω at both ends and nowhere else. The board and most toolheads have a jumper for this.
- Power the toolhead as its manual describes.

## Toolhead

Leave the toolhead's Klipper firmware (or Katapult bootloader) as it is. It must be built for CAN on the toolhead's CAN pins at 1000000 bit/s, or `CAN_BITRATE` here must be changed to match.

## Test

1. `M960` reports the bus state and counters, e.g. `CAN bitrate:1000000 state:active rx:0 tx:0 ...`. Before any other node answers, the first frames sent get no acknowledgment and the state can go to `error-passive`. A state that stays `bus-off`, or `tx_errors` that keep growing with the toolhead connected, points to wiring, termination or a bitrate mismatch.
2. `M960 Q` lists each CAN node that has no node ID yet, e.g. `CAN node uuid=0123456789ab app=Klipper`. If you have a Linux CAN adapter (such as a BigTreeTech U2C), Klipper's `scripts/canbus_query.py can0` should report the same UUID.
3. `M960 I` assigns node IDs from 4 up and reads each Klipper node's data dictionary, e.g. `nodeid=4 dictionary=4512 bytes adler32=...`.

A node keeps its ID until it is reset, so power-cycle the toolhead before repeating `M960 Q` or `M960 I`.

Please post the output of all three commands, the toolhead model and its Klipper version in the pull request.
