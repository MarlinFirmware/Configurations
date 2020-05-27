New build environment for MKS Robin with HAL STM32 with TFT and touch screen support
Works with framework-arduinoststm32 verions 3.107 and 4.107
For development and testing purposed only

Known issues:
 - SDIO is exteremely unstable
 - framework-arduinoststm32 has to be in .platformio\packages\framework-arduinoststm32
 - compiled firmware hangs at boot if framework-arduinoststm32 is located in .platformio\packages\framework-arduinoststm32@<version>

[https://github.com/MarlinFirmware/Marlin/issues/18129]
