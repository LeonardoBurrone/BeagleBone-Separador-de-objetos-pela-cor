import Adafruit_BBIO.PWM as PWM

servoPin="P9_14"
PWM.start(servoPin, 5, 50)

while(1):
        dutyCycle=input("What Duty Cycle? ")
        PWM.set_duty_cycle(servoPin, dutyCycle)
		
---------------------------------------------------

import Adafruit_BBIO.PWM as PWM
servoPin="P9_14"
PWM.start(servoPin, 5, 50)

while(1):
        desiredAngle=input("What Angle do You Want? ")
        dutyCycle=1./18.*desiredAngle + 5
        PWM.set_duty_cycle(servoPin, dutyCycle)
		
------------------------------------------------------------

import Adafruit_BBIO.PWM as PWM

servoPin="P9_21"
PWM.start(servoPin, 3, 50)

while(1):
        dutyCycle=input("What Duty Cycle? ")
        PWM.set_duty_cycle(servoPin, dutyCycle)
		
------------------------------------------------------------