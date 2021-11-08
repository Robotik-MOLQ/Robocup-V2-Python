from meinePins import *
import machine

TasterL = machine.Pin(TASTER_L, machine.Pin.IN, machine.Pin.PULL_DOWN)
TasterR = machine.Pin(TASTER_R, machine.Pin.IN, machine.Pin.PULL_DOWN)

def getTotalValue():
    val_L = TasterL.value()
    val_R = TasterR.value()
    return val_L, val_R, val_L + val_R