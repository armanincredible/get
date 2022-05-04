import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup (24, GPIO.OUT)
GPIO.setup (2, GPIO.OUT)

p = GPIO.PWM(24, 500)
res = GPIO.PWM(2, 500)

def decimal2binary (value):
    return [int(element) for element in bin (value)[2:].zfill(8)]

try:
    while 1:
        period = input ("write a cycle time\n")

        if period == 'q':
            break
            
        period = float (period)

        if (period >= 0 and period <= 100):
            p.start (period)
            res.start (period)
            print ("excepted: ", "{:.4f}".format(3.3 * period / 100), "v")

finally:
    p.stop ()
    GPIO.cleanup ()