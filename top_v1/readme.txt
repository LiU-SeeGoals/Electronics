This top PCB has an IMU sensor, socket for nRF module and four LED's
The nRF 5V connection has two decoupling capacitors for reducing noise.

IMPORTANT: J2 is used to power the PCB with the internal 3.3V power supply of the STM32Nucleo board.
If an external supply is needed, disconnect this jumper and connect the external power supply to the bottom most pin of J2.

Pin details

PD1 - LED1_RED
PD4 - LED2_BLUE
PD6 - LED3_WHITE
PD3 - LED4_BLUE 

PF14 - IMU_SCL
PF15 - IMU_SDA

PC6  - RF_CE
PB15 - RF_IRQ
PB8  - RF_CSN
PA5  - RF_SCK
PA6  - RF_MISO
PB5  - RF_MOSI
