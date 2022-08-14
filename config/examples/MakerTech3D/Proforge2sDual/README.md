
# Configurations tips for Proforge 2s Dual 

Below are possible Configurations tips:-


## Printer will not home
// Choose the name from boards.h that matches your setup

        #ifndef MOTHERBOARD
        #define MOTHERBOARD BOARD_MKS_GEN_L

        /**
        * Pin allocation for the inductive sensor. 
        * Thanks to  'ellensp' for the help in finding the correct pin.
        * 
        */
        
        #define Z_MIN_PIN 63  


## Proforge 2s dual servo motor switch over getting hot
        // Only power servos during movement, otherwise leave off to prevent jitter
        #define DEACTIVATE_SERVOS_AFTER_MOVE

<<<<<<< HEAD
## PID Turnig and problem with stable temperature
=======
## PID Turnig and problem with stable temp
>>>>>>> 8fff7fe123d072b19df125a3b278fe9d217b20be
        Enable EEPROM settings so that I can save PID turning.
        Enable PIDTEMPBED for the bed so that I can run PID turnung for the bed
        
        #define PID_DEBUG             // Print PID debug data to the serial port. Use 'M303 D' to toggle activation.
        #define PID_PARAMS_PER_HOTEND // Use separate PID parameters for each extruder (useful for mismatched extruders)


