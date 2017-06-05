import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
SWITCH = 19
GPIO.setup(SWITCH, GPIO.IN)

for i in range(200):
    print GPIO.input(SWITCH);
    time.sleep(.1);
