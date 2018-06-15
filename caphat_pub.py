#!/usr/bin/env python

import sys
import time
from pySpacebrew.spacebrew import Spacebrew
import RPi.GPIO as GPIO

import Adafruit_MPR121.MPR121 as MPR121

# Create MPR121 instance.
cap = MPR121.MPR121()
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)
# publish button press - bool
# listen for light changes - bool
brew = Spacebrew("MRHT_Light_Button", description="Python Light and Button controller",  server="192.168.1.165", port=9000)
#brew.addSubscriber("flipLight", "boolean")
brew.addPublisher("buttonPress", "boolean")

CHECK_FREQ = 0.1 # check mail every 60 seconds

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GREEN_LED = 18
#RED_LED = 23
#GPIO.setup(GREEN_LED, GPIO.OUT)
#GPIO.setup(RED_LED, GPIO.OUT)
#GPIO.setup(24, GPIO.IN)
#lightOn = False

#def handleBoolean(value):
  #  global lightOn
    # print("Received: "+str(value))
    #if (value == 'true' or str(value) == 'True'):
      #  lightOn = not lightOn
        #GPIO.output(GREEN_LED, True)

#brew.subscribe("flipLight", handleBoolean)


last_touched = cap.touched()
# while True:
#     current_touched = cap.touched()
#     # Check each pin's last and current state to see if it was pressed or released.
#     for i in range(12):
#         # Each pin is represented by a bit in the touched value.  A value of 1
#         # means the pin is being touched, and 0 means it is not being touched.
#         pin_bit = 1 << i
#         # First check if transitioned from not touched to touched.
#         if current_touched & pin_bit and not last_touched & pin_bit:
#             print('{0} touched!'.format(i))
#         # Next check if transitioned from touched to not touched.
#         if not current_touched & pin_bit and last_touched & pin_bit:
#             print('{0} released!'.format(i))
#     # Update last state and wait a short period before repeating.
#     last_touched = current_touched
#     time.sleep(0.1)


try:
    brew.start()
    #print("Should be looping")
    print("Press Ctrl-C to quit.")
    while True:
        #print("LOOP")
 #       GPIO.output(GREEN_LED, False)
        if cap.is_touched(0):
		    print("Button 0 Pushed")
		    brew.publish('buttonPress', True)
  #      GPIO.output(GREEN_LED, lightOn)
        time.sleep(CHECK_FREQ)
    
finally:
    GPIO.cleanup()
    brew.stop()


