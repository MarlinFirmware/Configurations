# 3D Printed DIY CNC by Aviran N
### Used hardware
- [BIGTREETECH SKR Mini E3 V3](https://github.com/bigtreetech/BIGTREETECH-SKR-mini-E3)
- **Modded** [Anet 2004 LCD with 5 buttons](https://shop.anet3d.com/collections/accessories-for-anet-a8/products/a8-lcd-screen)

### WARNING - DO NOT CONNECT THE 20x4 LCD SCREEN WITHOUT PROPER MODIFICATIONS! YOU MAY CAUSE DAMAGE TO THE BOARD!
You can find detailed instructions of necessary modifications [here](https://gist.github.com/Caraffa-git/840b798517e7ee01ab47fabf6271b9c4).

### Additional informations
The driver assigned to the extruder (E0) was used as a second Y axis controller, for this reason a pin reassignment in the file `Marlin/src/pins/stm32g0/pins_BTT_SKR_MINI_E3_V3_0.h` is required.

To prevent the loss of steps, the currents of the X and Y drivers were increased. In case this value would not be sufficient or the drivers would overheat, the set currents in the `Configuration_adv.h` file should be changed. 

CNC project: https://www.printables.com/pl/model/129795-3d-printed-diy-cnc-dremel-cnc-remix 
