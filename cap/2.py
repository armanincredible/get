import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup (dac, GPIO.OUT)

def decimal2binary (value):
    return [int(element) for element in bin (value)[2:].zfill(8)]

try:
    while 1:
        print ("write a cycle time")
        period = float (input())
        period = period / 512
        for i in range (255):
            GPIO.output (dac, decimal2binary(i))
            time.sleep(period)
        i = 255
        while i > 0:
            GPIO.output (dac, decimal2binary(i))
            time.sleep(period)
            i = i -1

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup ()