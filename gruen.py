from meinePins import *
from allSensors import *

greenLoop = [0,0]  # nicht die Länge verändern!

def aufGruen(richtung):
    if richtung == LINKS:
        diff = sensor_G.wertL - sensor_R.wertL
    else:
        diff = sensor_G.wertR - sensor_R.wertR
        
    if diff >= GRUENSCHWELLE:
        if greenLoop[richtung] > 4:
            return True
        else:
            greenLoop[richtung] += 1
            return False
    else:
        greenLoop[richtung] = 0
        return False
        
    

