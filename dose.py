from motor import *
import utime
from meinePins import *
from Bewegungsablauf import *


ZeitR = [
    1.000,
    1.100,
    1.600,
    1.100,
    2.000,
    1.000,
    1.500,
    1.000
    ]

MotR  = [
    MOT_AB,
    MOT_B,
    MOT_AB,
    MOT_A,
    MOT_AB,
    MOT_A,
    MOT_AB,
    MOT_B
    ]

V2 = [
    (-40,-40),
    (-40,40),
    (40,40),
    (40,-40),
    (40,40),
    (40,-40),
    (40,40),
    (-40,40)
    ]

class Ablauf():
    def __init__(self,Mot,Time,V,abbruch = False):
        self.Mot = Mot
        self.Time = Time
        self.V = V
        self.abbr = abbruch
    def run(self):
        for ix in range(len(self.Mot)):
            OnFwd(MOT_A,self.V[ix][0])
            OnFwd(MOT_B,self.V[ix][1])
            utime.sleep(self.Time[ix])
            #sensor_W.messen()
            #if self.abbr and sensor_w.wertL < 20
            #    break
            
DoseUmfahren = Ablauf(MotR,ZeitR,V2)