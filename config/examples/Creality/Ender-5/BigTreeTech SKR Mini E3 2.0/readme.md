# Ender-5 BigTreeTech SKR Mini E3 v2.0 configuration

Edit `platformio.ini` section `[platformio]`, change `default_envs` as shown:

    default_envs = STM32F103RC_btt_512K


**Note** This Configuration.h contains settings for newer leadscrew with 800 steps/mm. If your printer has older leadscrew, change pre
`DEFAULT_AXIS_STEP_PER_UNIT` to have 400 for the Z axis as in the example below.

    #define DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 400, 93 }
