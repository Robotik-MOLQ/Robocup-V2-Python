from motor import *
import utime
from meinePins import *
from Bewegungsablauf import *

V2 = 70

ZeitR = [
    1.500,
    0.500,
    1.000,
    0.500,
    1.000,
    0.500,
    1.000,
    0.500
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



class Ablauf():
    def __init__(self,Mot,Time,V,abbruch = False):
        self.Mot = Mot
        self.Time = Time
        self.V = V
        self.abbr = abbruch
    def run(self):
        for ix in range(len(self.Mot)):
            OnFwd(self.Mot[ix],70)
            utime.sleep(self.Time[ix])
            #sensor_W.messen()
            #if self.abbr and sensor_w.wertL < 20
            #    break
            
DoseUmfahren = Ablauf(MotR,ZeitR,V2)