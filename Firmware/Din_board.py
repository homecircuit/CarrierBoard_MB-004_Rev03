import time
import RPi.GPIO as GPIO

# Pins definitions
din_pins = [4,23,5,12,6,16,20,21]

din_port = 0x00
din_idx = 0

# Set up pins
GPIO.setmode(GPIO.BCM)
for pin in din_pins:
    GPIO.setup(pin,GPIO.IN)

# If button is pushed, light up LED
try:
    while True:
        for pin in din_pins:
            logic = GPIO.input(pin)
            #print('pin:{0}: {1:b}'.format(din_idx,logic))
            din_port|=(logic<<din_idx)
            #print('byte val {0}: {1:b}'.format(din_idx,din_port))
            #print('pin idx:{0}'.format(din_idx))
            din_idx+=1
        time.sleep(1)
        print('port val: {0:02X} {0:b}'.format(din_port))
        din_idx=0
        din_port = 0
# When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()
