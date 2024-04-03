# Electronics

The electronics are currently divided into:
- [Nucleo - devboard with STM32](#item-one)
- [Powerboard](#item-two)
- [Motor drivers](#item-three)
- [Drive motors](#item-four)
- [Dribbler motor](#item-five)
- [Kicker board](#item-six)
- [Kicker solenoid(s)](#item-seven)
- [IR beam and dribbler motor sensor](#item-eight)
- [Tranciever board](#item-nine)
- [Battery](#item-ten)
- [Base station](#item-eleven)
  
<!-- headings -->
<a id="item-one"></a>
### Nucleo
A devboard with a STM32 which is the processor of the robot.

<a id="item-two"></a>
### Powerboard
The powerboard is the connection point of the battery and supplies the robot with: battery voltage, 12V, 5V and 3.3V. It also acts as a holder for the motor driver boards. The powerboard serves as a central connection point and is connected to: the nucleo board, the motor drivers, the kicker board (12 pin 1.25 mm spacing single row), IR beam (2x 3 pin 1.25 mm), the battery.

The battery is connected via a battery management circuit (BMS).

<a id="item-three"></a>
### Motor drivers
Second item content goes here

<a id="item-four"></a>
### Drive motors
Second item content goes here

<a id="item-five"></a>
### Dribbler motor
Second item content goes here

<a id="item-six"></a>
### Kicker board
The kicker board is taken from [TIGERs 2020 version](https://github.com/TIGERs-Mannheim/electronics) (open source). Schematics and pictures can be found in this repository as well as various files. The design uses a LT3751FE High Voltage Capacitor Charger Controller and a DA2034-AL transformer to charge two 1800uF 250V connected in parallel. By discharging the capacitors through the kicker (or chiper) solenoid a powerfull impact is created. The board also contains a temperature sensor and charge voltage reader that is connected to an A/D converter which is accessed with SPI. The main power to the capasitors come from the Vcc pin, which is connected to battery voltage.

Further reading can be found in the kicker repository.

<a id="item-seven"></a>
### Kicker solenoid
Currently a [12V "long travel" solenoid from Amazon](https://www.amazon.com/Abletop-Solenoid-Electromagnetic-Electric-Automobiles/dp/B07G15X91N) is used as the kicker solenoid, this has worked well so far but the solenoid is heavy and too large to fit a second solenoid for chipping. Therefore custom made solenoids should eventually be made, TIGERs uses a flat design in order to maximize power but several other teams use two cylindrical solenoids stacked.

Further reading can be found in the kicker repository.

<a id="item-eight"></a>
### IR beam and dribbler motor sensor
Currently the IR beam design for ball sensing, from [TIGERs 2016 version](https://www.tigers-mannheim.de/index.php?id=65) is used. Note that TIGERs 2020 version also uses an array of IR LEDs and sensors from above the ball. The beam consists of one small transmitter pcb (VSMB2000X01 IR LED) and one reciever (TEMD1000) on either side of the dribbler assembly. A beam is continuously transmitted and is broken when a ball is at the dribbler. The dribbler motor temperature sensor is taken from TIGERs 2020 version but will preliminarilly be connected directly to the nucleo board via the powerboard. 

<a id="item-nine"></a>
### Tranciever board
The tranciever board is connected to the nucleo board and enables wireless comunication via the robots and the base station.

<a id="item-ten"></a>
### Battery
Second item content goes here

<a id="item-eleven"></a>
### Base station
Second item content goes here
