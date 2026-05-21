from machine import Pin
from time import sleep

redled = Pin(15, Pin.OUT)

while True:
    redled.value(1)
    sleep(1)
    redled.value(0)
    sleep(1)