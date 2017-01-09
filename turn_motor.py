import RPi.GPIO as GPIO
import time

PIN1 = 20
PIN2 = 26


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)

try:
    while True:
        GPIO.output(PIN1, True)
        GPIO.output(PIN2, False)
        time.sleep(1)

        GPIO.output(PIN1, False)
        GPIO.output(PIN2, False)
        time.sleep(0.1)

        GPIO.output(PIN1, False)
        GPIO.output(PIN2, True)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

