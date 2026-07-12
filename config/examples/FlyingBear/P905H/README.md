# Flying Bear P905H

Configuration is based on P905H with **a single extruder and inductive Z-sensor**.

I've tried to adapt original Marlin 1.x limits to Marlin 2.1.x with classical jerk and linear advance enabled.

 - Linear advance is working but CPU can not handle high speed (more than 90 mm/s or even less)
 - Because P905 has heavy X and even heavier Y mass you should consider lower jerk values compared to other printers
 - Turning off linear advance/jerk could let you print faster but you should lower print acceleration to 200 (as it was in manufacturer config)
 
There are some comments in the code that you can find by "P905H" keyword.
