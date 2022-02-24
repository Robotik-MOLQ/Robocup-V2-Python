#from meinePins import *
from Motor import *
import utime

#-------------------------------------------------
TASTER_LR = 16

def doseUmfahren():
    if TASTER_LR > 0:
        OnRev( MOT_AB, 70)
        utime.sleep_ms(1500)
        OnFwd( MOT_B, 70)
        utime.sleep_ms(500)
        OnFwd( MOT_AB, 70)
        utime.sleep_ms(1000)
        OnFwd( MOT_A, 70)
        utime.sleep_ms(500)
        OnFwd( MOT_AB, 70)
        utime.sleep_ms(1000)
        OnFwd( MOT_A, 70)
        utime.sleep_ms(500)
        OnFwd( MOT_AB, 70)
        utime.sleep_ms(1000)
        OnFwd( MOT_B, 70)
        utime.sleep_ms(500)
doseUmfahren()
        