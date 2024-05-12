# Velleman K8400 Vertex Configuration

Source: [velleman.eu](https://www.velleman.eu/products/view/?id=417866)

Configuration files for the K8400, ported upstream from the official Velleman firmware.
Like its predecessor, (K8200), the K8400 is a 3Drag clone. There are some minor differences, documented in `pins_K8400.h`.

Single- and dual-head configurations provided. Copy the correct `Configuration.h` and `Configuration_adv.h` to the `/src/config` directory.

> [!NOTE]
> This configuration includes the community sourced feed rate fix. Use 100% feed rate in Repetier!

### Original Sources

Upstreamed from:

[birkett/Vertex-K8400-Firmware on GitHub](https://github.com/birkett/Vertex-K8400-Firmware)

Credit to Velleman for the original Marlin 1.0.x based code:

- [Download Vertex M1 1.4-H1](https://cdn.velleman.eu/downloads/files/vertex/firmware/vertex-m1-v1.4-h1.zip)
- [Download Vertex M1 1.4-H2](https://cdn.velleman.eu/downloads/files/vertex/firmware/vertex-m1-v1.4-h2.zip)
