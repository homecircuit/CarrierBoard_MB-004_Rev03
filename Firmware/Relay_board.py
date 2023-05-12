import RPi.GPIO as GPIO
import time
relay_pins = [17,18,27,22]
GPIO.setmode(GPIO.BCM)
for pin in relay_pins:
    GPIO.setup(pin,GPIO.OUT) 

for pin in relay_pins:
    print('pin {0}'.format(pin))
    GPIO.output(pin,True)
    time.sleep(1)
    GPIO.output(pin,False)
    time.sleep(1)
    #print('pin {0}'.format(pin))
GPIO.cleanup()
