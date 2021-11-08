import utime
import taster
import display
from motor import *
from meinePins import *
from dose import *
from sensor_Licht import *
#from datei import *

#------------------------------------------------------
diff = 0

sensor_A = Sensor(LED_A, "Außen")
sensor_W = Sensor(LED_W, "Weiss")
sensor_R = Sensor(LED_R, "Rot")
sensor_G = Sensor(LED_G, "Gruen")
sensoren = [sensor_W,sensor_R,sensor_A]
#------------------------------------------------------
Off(MOT_AB)
for s in sensoren: #startet Kalibrierung
    s.kalibrierStart()

for i in range (1000): # Kalibrierung
    for s in sensoren:
        s.kalibrierRunde()

# for s in sensoren:
#     print(s.name, s.miniL, s.maxiL, s.miniR, s.maxiR) # Bildschirmausgabe der Werte


#for i in range (3000): 
#    for s in sensoren:
#        s.messen()
#        print(s.name, s.wertL, s.wertR)


while True: # Linienfolger 
    for s in sensoren: # messen der Lichtwerte 
        s.messen()
#         STR = str(s.wertl) + " " + str(s.wertR)
#         display.schreibe(STR)
#         display.oled.shift
    if taster.getTotalValue()[2] > 0: # bei betätigung der Taster
        DoseUmfahren.run()              # Dose umfahren 
    diff = sensor_W.wertL - sensor_W.wertR # Differenz bilden 
    diff = diff*2 # die Differenz mal 2, um den Bewegungsfaktor zu erhöhen
    if sensor_A.wertL - sensor_A.wertR > 75:
        diff = 200
    elif sensor_A.wertR - sensor_A.wertL > 75:
        diff = -200
    OnFwd(MOT_B,V - diff) # Geschwindigkeit wird auf verschidene Werte gesetzt
    OnFwd(MOT_A,V + diff)
    
    
   
    