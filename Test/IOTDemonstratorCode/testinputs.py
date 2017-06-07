import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
SWITCH = 21
GPIO.setup(SWITCH, GPIO.IN)
OUT=26
GPIO.setup(OUT,GPIO.OUT)

for i in range(50):
    if i/2 = 1:
        GPIO.output(OUT,True);
    else:
        GPIO.output(OUT,False);
    time.sleep(.1);
    print GPIO.input(SWITCH);
