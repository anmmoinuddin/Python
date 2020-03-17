import RPi.GPIO as GPIO
from time import sleep

#setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

while True:
      sensor=GPIO.input(27)

      if sensor==1:
            print(" I See you...")
            sleep(0.1)
      elif sensor==0:
            print("OH no")



