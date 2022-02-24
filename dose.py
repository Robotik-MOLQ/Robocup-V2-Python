from motor import *
import utime
from sensor_Licht import *
from meinePins import *
from Bewegungsablauf import *
from allSensors import *

def TestenUndFahren(Va,Vb,t):
    t1 = utime.ticks_ms()
    diff = 0
    OnFwd(MOT_A,Va)
    OnFwd(MOT_B,Vb)
    while diff < t:
        sensor_W.messen()
        if sensor_W.wertR < 20:
            Off(MOT_AB)
            return True
        diff = utime.ticks_ms() - t1
    Off(MOT_AB)
    return False

def run():
    OnFwd(MOT_AB,-40)
    utime.sleep(0.5)
    OnFwd(MOT_B,40)
    utime.sleep(1.1)
    OnFwd(MOT_AB,40)
    utime.sleep(0.4)
    Off(MOT_AB)
    utime.sleep(0.5)
    Linie = False
    Linie = TestenUndFahren(50,50,500)
    while not Linie:
        Linie = TestenUndFahren(50,-50,300)
        if Linie:
            break
        Linie = TestenUndFahren(50,50,500)