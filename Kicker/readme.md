# Kicker

The kicker board is taken from [TIGERs 2020 version](https://github.com/TIGERs-Mannheim/electronics) (open source). Schematics and pictures can be found in this repository as well as various files. The design uses a LT3751FE High Voltage Capacitor Charger Controller and a DA2034-AL transformer to charge two 1800uF 250V connected in parallel. By discharging the capacitors through the kicker (or chiper) solenoid a powerfull impact is created. The board also contains a temperature sensor and charge voltage reader that is connected to an A/D converter which is accessed with SPI. The main power to the capasitors come from the Vcc pin, which is connected to battery voltage.

### PCB design
From TIGERs 2020 ETDP:

"The kicker circuit is responsible for charging a set of capacitors to a high voltage 
and discharging them through the kicker coils to kick the ball. The kick strength 
is directly proportional to the current owing through the coil. The current 
depends on resistance of the coil and supplied voltage. To achieve kick speeds 
up to the league limit of 6.5m/s a high voltage is required. The v2020 design 
uses a software-controlled soft-limit of 240V and a hardware-enforced hard-limit 
of 250V. A pair of capacitors with 250V rating and 1800µF are used, yielding a 
total of 3600µF and a stored energy of 112.5J. The capacitors are used together 
for a coil, not one capacitor per coil. 
The charge circuit uses a yback converter topology based on the Analog 
Devices6 LT3751 capacitor charge IC [13]. This circuit can charge the capacitors 
form 0V to 250V in two seconds. Recharging after a strong kick takes half a 
second. An advantage of the yback topology is the isolation of high voltage 
areas from the rest of the electronics. 
The kicker board does not have its own microcontroller. It is intentionally 
designed to be very simple to reduce the risk of fatal mistakes. It only has a 
SPI interface to an ADC, used to monitor capacitor voltage and two input lines 
to trigger a at or chip kick. These trigger lines are digitally isolated from the 
high-voltage area. The primary microcontroller monitors the capacitor voltage 
and stops charging at 240V. This is the normal operating mode. If this fails for 
any reason the LT3751 is congured for a hard-limit of 250V to ensure capacitors 
are never overcharged. 
It is absolutely vital to design the kicker circuit as safe as possible and to 
do a proper failure analysis and mitigation plan. Failure to do so can result in 
serious injuries. As an additional safety measure our robots always discharge 
themselves upon shutdown. This way we can be relatively sure that a turned-on 
robot is also safe to touch and work on."

### Solenoid
Currently a [12V "long travel" solenoid from Amazon](https://www.amazon.com/Abletop-Solenoid-Electromagnetic-Electric-Automobiles/dp/B07G15X91N) is used as the kicker solenoid, this has worked well so far but the solenoid is heavy and too large to fit a second solenoid for chipping. Therefore custom made solenoids should eventually be made, TIGERs uses a flat design in order to maximize power but several other teams use two cylindrical solenoids stacked.

Personel at the university noted that it is unusual to make flat solenoid. They instead recommended drilling out the core in order to lower the moving weight while still keeping most of the magnetic properties. 

We are looking into simpler 3D-printed designs, which uses a screw or similar as a core. For example [RobôCIn 2019](https://tdp.roboteamtwente.nl/tdps/225?ref=year) (which is based on [Immortals 2018 design](https://github.com/Ma-Ghasemieh/Immortals_ssl_opensource_mech)).  

### PCB ordering process
We ordered the pcbs from jlcpcb.com, they are cheap and we have not encountered any problems so far. The design features a number of non standard components which are more expensive and of which some had to be ordered via their global shipping option. It is also important to note that a large share of the cost came from the more expensive components, an IC from TI for example can cost $ 5-10. 

Jlcpcb does use an automatic component search function, which mostly worked, but some components had to be manually changed. The BOM and CPL where generated from TIGERs eagle files using [jlcpcbs eagle UPL](https://jlcpcb.com/help/article/82-How-to-generate-BOM-and-CPL-from-Eagle-CAD-automatically). 

