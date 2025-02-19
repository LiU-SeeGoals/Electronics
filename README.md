# Electronics
Schematics etc.

# Motor driver

The motor driver has 5 important pins, 

Motor driver has 5 pins to the devboard, 2 power pins and 8 pins to the motor 

The important pins are
```
PWM, - Takes PWM signal to decide speed of motor, generate from devboard with timers.

FGOUT, - Hall sensor tick output, work like a wheel encoder and ticking as the motor spins so that we know how much the motor has spun.

nFault, - Gives fault messages when fault states are entered by going low. Currently does not work, set this pin HIGH 5v or motor driver can enter test mode.

brake - HIGH sets all motor coils high breaking the motor hard.

dir - Decides direction for motor
```

## Motor driver improvements

Capacitors and components change capacitance, inductance, etc as the voltage changes. 
This was not know during the making of driver.

Capacitors should be closer to the pins they are filtering.

There is a risk of overheating if the motors get stuck for a longer time, adding some cooling would be nice.


## Getting started

Add the .pretty library file to get footprints from lib/

Using kicad: preferences -> Manage footprint libraries

