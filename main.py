import utime
import taster
import display
from motor import *
from meinePins import *
from dose import *
from sensor_Licht import *
import speicher
#from datei import *

#------------------------------------------------------
diff = 0

sensor_A = Sensor(LED_A, "Außen")
sensor_W = Sensor(LED_W, "Weiss")
sensor_R = Sensor(LED_R, "Rot")
sensor_G = Sensor(LED_G, "Gruen")
sensoren = [sensor_W,sensor_R,sensor_A,sensor_G]
#------------------------------------------------------
Off(MOT_AB)


display.leereDisplay()
display.schreibe("Ready")
display.schreibe("LINKS => Kal.",2)
display.schreibe("RECHTS => laden",3)

waiting = True
while waiting:
    if taster.getTotalValue()[1] > 0:
        speicher.LadeWerte(sensor_W,sensor_A,sensor_R,sensor_G)
        waiting = False
    elif taster.getTotalValue()[0] > 0:
        display.leereDisplay()
        display.schreibe("Kalibrieren...",2)
        for s in sensoren: #startet Kalibrierung
            s.kalibrierStart()
        for i in range (1000): # Kalibrierung
            for s in sensoren:
                s.kalibrierRunde()
        speicher.SchreibeWerte(
            [sensor_W.miniL,sensor_W.maxiL,sensor_W.miniR,sensor_W.maxiR],
            [sensor_A.miniL,sensor_A.maxiL,sensor_A.miniR,sensor_A.maxiR],
            [sensor_R.miniL,sensor_R.maxiL,sensor_R.miniR,sensor_R.maxiR],
            [sensor_G.miniL,sensor_G.maxiL,sensor_G.miniR,sensor_G.maxiR]
        )
        waiting = False

utime.sleep(0.5)



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
        display.leereDisplay()
        display.schreibe("Doose")
    diff = sensor_W.wertL - sensor_W.wertR # Differenz bilden 
    diff = diff*2 # die Differenz mal 2, um den Bewegungsfaktor zu erhöhen
    if sensor_A.wertL - sensor_A.wertR > 75:
        diff = 200
    elif sensor_A.wertR - sensor_A.wertL > 75:
        diff = -200
    OnFwd(MOT_B,V - diff) # Geschwindigkeit wird auf verschidene Werte gesetzt
    OnFwd(MOT_A,V + diff)
    
    
   
    