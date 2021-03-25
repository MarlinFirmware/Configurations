Marlin 2.0.7.2 for CR-10 Mini w/BL Touch

This firmware is configured for the BigTreeTech SKR E3 Mini V2 in a Creality CR-10 Mini
using the stock CR-10 display, and a BL Touch v3.1 ABL probe mounted on a Bullseye fan duct.
There are additional features enabled to take advantage of the capabilities of the BTT SKR E3 Mini V2 board
which will be detailed below. 
 
Compile this in the STM32F103RC_btt_512K environment.  My board came with 512K of ROM and this firmware will
use a little over half of that.  If your board only has 256K, you will have to disable some features in order
to make the firmware fit.
 
Configuration.h notes:

#define USE_PROBE_FOR_Z_HOMING
****  This configuration uses only the probe for Z homing.  The Z-stop switch is NOT enabled and can be disconnected. 

#define Z_MIN_PROBE_PIN PC14  //Zstop Pin in Z-Probe port 
****  Plug the BL Touch Blk/Wht connector in to the top two pins of the 5 pin Z-Probe port with the white whire "up". Do not plug the connector in to the Z-min port where the limit switch was plugged in.

#define NOZZLE_TO_PROBE_OFFSET { -38, -8, 0 }
****  These are the offsets for a left-side mounted BL Touch on a Bullseye fan duct base.  Change them as required for your particular BL Touch mount.

#define MULTIPLE_PROBING 2
****  Bed probing will test each point twice.  1st probe will be "fast" Z, 2nd will use the slower Z rate.

#define Z_MIN_PROBE_REPEATABILITY_TEST
****  M48 Enabled to establish probe deviation value.

#define AUTO_BED_LEVELING_BILINEAR
****  Change this as desired.  BILINEAR will work for most printers.

//#define RESTORE_LEVELING_AFTER_G28
****  This was disabled after discovering that sometimes, even with an M420 command in start G-Code, ABL would toggle to the opposite of whatever the ABL state was (Enabled/Disabled) at the time a print job started. 

#define GRID_MAX_POINTS_X 5
****  This configuration is set to use a 5x5 (25 point) probing grid.  Change as desired. 

#define EXTRAPOLATE_BEYOND_GRID
****  By default, this is disabled.  Enabling this seemed to provide better mesh data.
 
#define LCD_BED_LEVELING
****  Provides control panel probe controls.
 
#define LEVEL_BED_CORNERS 
****  Provides control panel bed tramming controls.

#define Z_SAFE_HOMING
****  Ensures the BL Touch probe is not hanging off the edge of the bed when Z homing.

#define CR10_STOCKDISPLAY
****  If you are using the stock display on your CR-10 Mini, this **MUST** be enabled.

Configuration_adv.h notes:

#define LIN_ADVANCE
****  This is enabled, but the K value is set to 0 which effectively disables LIN_ADVANCE.  Calibrate Linear Advance and set your own K value and recompile.

#define ARC_SUPPORT               // Disable this feature to save ~3226 bytes
****  Enables G2/G3 moves to smooth curves in your prints.  Required for the Arc Welder plugin for OctoPrint etc.

#define ARC_P_CIRCLES           // Enable the 'P' parameter to specify complete circles
****  Normally disabled by default. 

 






 
 