import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO_TRIGGER = 11
GPIO_ECHO = 13
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
print("Sensor ready") 
def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    ct=0
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        ct+=1
        if ct>5000:
            return(0)
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance


while 1 :
        print(distance())
