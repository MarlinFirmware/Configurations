# Ender-3 with a CR-10S board

This config is for an Ender-3 retrofitted with a CR-10S V2.1 board (but using
the original Ender-3 LCD). I wanted the expanded memory of the CR10-S board so
that I could enable BLTouch without having to disable features, due to the
limited memory in the original board.

## Enabled features

It has the BLTouch enabled and configured for the Creality BLTouch kit and
mounting bracket. The outer probe points are positioned over the springs.
Also corder levelling menu is enabled to allow the springs to be adjusted.

It has S-curve acceleration enabled, and some tweaks to the jerk settings to
prevent layer skips, and in general produce less shaking while printing.

## Special notes

On the Ender-3 the hotend is capable of traveling to the right well past the
print surface. In order to allow the BLTouch to probe the full surface of the
bed, Marlin has been configured to allow the X-axis to move out to 240mm. This
should be fine for any standard Ender-3, but something to be aware of if you
have modified anything that may cause a machine crash when doing so.
