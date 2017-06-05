# A network switch server - showing a remotely polled switch
#
# Any message from the client causes this server to send the 
# present status of the switch

import RPi.GPIO as GPIO
import time
import network

SWITCH = 19
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SWITCH, GPIO.IN)

def heard(phrase):
  print "heard:" + phrase
  for a in phrase:
    if a == "\r" or a == "\n":
      pass # strip it
    else:
      if (GPIO.input(SWITCH)):
        network.say("1")
      else:
        network.say("0")

while True:
  print "waiting for connection"
  network.wait(whenHearCall=heard)
  print "connected"
  
  while network.isConnected():
    print "server is running"  
    time.sleep(1)
    
  print "connection closed"
  
  
# END
