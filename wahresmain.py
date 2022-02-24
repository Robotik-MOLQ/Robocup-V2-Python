import utime
import taster
import display
from motor import *
from meinePins import *
import dose
from sensor_Licht import *
import speicher
#from datei import *
from allSensors import *
#------------------------------------------------------
diff = 0


#------------------------------------------------------
Off(MOT_AB)


display.leereDisplay()
display.schreibe("Init Complte!")
display.schreibe("RECHTS => Kalibrieren",2)
display.schreibe("LINKS => laden",3)

waiting = True
while waiting:
    if taster.getTotalValue()[1] > 0:
        speicher.LadeWerte([sensor_W,sensor_A,sensor_R,sensor_G])
        waiting = False
    elif taster.getTotalValue()[0] > 0:
        display.leereDisplay()
        display.schreibe("Kalibrieren...",2)
        for s in sensoren: #startet Kalibrierung
            s.kalibrierStart()
        for i in range (500): # Kalibrierung
            for s in sensoren:
                s.kalibrierRunde()
        speicher.SchreibeWerte([sensor_W,sensor_A,sensor_R,sensor_G])
        print(sensor_W.miniL,sensor_W.maxiL,sensor_W.miniR,sensor_W.maxiR)
        waiting = False
        

utime.sleep(0.5)



# for s in sensoren:
#     print(s.name, s.miniL, s.maxiL, s.miniR, s.maxiR) # Bildschirmausgabe der Werte


#for i in range (3000): 
#    for s in sensoren:
#        s.messen()
#        print(s.name, s.wertL, s.wertR)

display.leereDisplay()
display.schreibe("main")
while True: # Linienfolger
    Gruen = 0
    for s in sensoren: # messen der Lichtwerte 
        s.messen()
    print("Gruen",sensor_G.wertL,"\tRot",sensor_R.wertL,"Gruen",sensor_G.wertR,"\tRot",sensor_R.wertR)
    gruenDiff = sensor_G.wertL - sensor_R.wertL
    print("")
    print(gruenDiff)
    if gruenDiff <= 10 and gruenDiff > 1:
        print("")
        print("Gruen")
    elif gruenDiff >= 10:
        print("")
        print("nicht Gruen")



#         STR = str(s.wertl) + " " + str(s.wertR)
#         display.schreibe(STR)
#         display.oled.shift
    if taster.getTotalValue()[2] > 0: # bei betätigung der Taster
        display.leereDisplay()
        display.schreibe("Dooooose")
        dose.run()              # Dose umfahren
        Off()
        display.leereDisplay()
        display.schreibe("main")
    diff = sensor_W.wertL - sensor_W.wertR # Differenz bilden
    Adiff = sensor_A.wertL - sensor_A.wertR
#     if sensor_G.wertL > sensor_R.wertL + 20:
#         Off()
#         display.leereDisplay()
#         display.schreibe("Gruen: {}".format(Gruen))
#         Gruen += 1
#         uteime.sleep(0.5)
#     else:
#         Gruen = 0
    #diffA = sensor_A.wertL - sensor_A.wertR
    diff = diff*2 # die Differenz mal 2, um den Bewegungsfaktor zu erhöhen
    if sensor_A.wertL - sensor_A.wertR > 60:
        diff = 500
        OnFwd(MOT_A,   diff)
        OnFwd(MOT_B,  -diff)
    elif sensor_A.wertR - sensor_A.wertL > 60:
        diff = -500
        OnFwd(MOT_A,   diff)
        OnFwd(MOT_B,  -diff)
    else:
        OnFwd(MOT_B,V - (diff + Adiff) /2) # Geschwindigkeit wird auf verschidene Werte gesetzt
        OnFwd(MOT_A,V + (diff + Adiff) /2)
    
    
    
   
    