from machine import *
from Motor import *
import utime

lichtW = Pin(20,Pin.OUT)
lichtR = Pin(19,Pin.OUT)
lichtG = Pin(18,Pin.OUT)
LEDs = [lichtW,lichtR,lichtG]

for i in range (10):
    for s in LEDs:
        s.value(1)
        utime.sleep(1)
        s.value(0)
        utime.sleep(1)


while True:
    utime.sleep(3)
    print("An")
    Off(MOT_AB)
    utime.sleep(3)
    print("Aus")