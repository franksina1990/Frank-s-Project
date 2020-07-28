
import time
import datetime
import RPi.GPIO as GPIO
import pandas as pd

GPIOpin = -1

# Initial Pin
def initialInductive(pin):
    global GPIOpin
    GPIOpin = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOpin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    print("Finished Initiation")
    print(GPIOpin)
    
while True:
    initialInductive(17)
    print(GPIO.input(GPIOpin))
    time.sleep(.1)