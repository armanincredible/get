import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup (dac, GPIO.OUT)

def decimal2binary (value):
    return [int(element) for element in bin (value)[2:].zfill(8)]

try:
    while 1:
        print("write a num")
        input_value = int (input())

        if input_value > 255:
            print ("uncorrect num")
            break
        
        if input_value < 0:
            print ("Uncorrect num")
            break
        
        currency = input_value/256 * 3.3
        print ("Voltage:", currency, "B")

        GPIO.output (dac, decimal2binary(input_value))

        time.sleep(5)

except ArithmeticError:
    value = 0

else:
    print ("No exceptions")

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup ()