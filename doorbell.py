#!/usr/bin/env python

import subprocess
import RPi.GPIO as GPIO
import time
print("Start script doorbell")
#subprocess.run(["ffplay","-nodisp","-t","15","-ss","40","-autoexit","FinalCountdown.mp3"])
pinnr1 =21
GPIO.setmode(GPIO.BCM)
pinnr2 =20
pinnr3= 16
GPIO.setup(pinnr1,GPIO.OUT)
GPIO.setup(pinnr2,GPIO.OUT)
GPIO.setup(pinnr3,GPIO.IN,pull_up_down=GPIO.PUD_UP)


while True:
    inputpin= GPIO.input(pinnr3)
    if inputpin== 0:
        GPIO.output(pinnr1,GPIO.HIGH)
        GPIO.output(pinnr2,GPIO.LOW)
        print("led on , button pushed")
        subprocess.run(["ffplay","-nodisp","-t","15","-ss","40","-autoexit","FinalCountdown.mp3"])
    else:
        GPIO.output(pinnr1,GPIO.LOW)  
        GPIO.output(pinnr2,GPIO.HIGH)
    time.sleep(0.01)


