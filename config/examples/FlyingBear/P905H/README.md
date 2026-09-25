# Flying Bear P905H

Configuration is based on P905H with **a single extruder and inductive Z-sensor**.

I've tried to adapt original Marlin 1.x limits to Marlin 2.1.x with classical Jerk and Linear Advance enabled.

 - Linear Advance is working but CPU can not handle high speed (more than 90 mm/s or even less).
 - Because P905H has heavy X and even heavier Y mass you should consider lower jerk values compared to other printers.
 - Turning off linear advance/jerk may allow faster printing, but reduce print acceleration to 200 (as in factory config).
 
Additional comments in the configurations are annotated with "P905H".
