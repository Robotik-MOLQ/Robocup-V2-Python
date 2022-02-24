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
from gruen import *
#------------------------------------------------------
diff = 0


#------------------------------------------------------
Off(MOT_AB)


display.leereDisplay()
display.schreibe("Init Complte!")
display.schreibe("LINKS => Kalibrieren",2)
display.schreibe("RECHTS => laden",3)

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
display.schreibe("Lutetium(g)")
display.schreibe("Deine Mudda",2)
display.schreibe("ich bin cool",3)
utime.sleep(2)
display.leereDisplay()
display.schreibe("main")
while True: # Linienfolger
    for s in sensoren: # messen der Lichtwerte 
        s.messen()
#     if aufGruen(LINKS):
#         print("GRUEeN")
#     else:
#         print("Im LINKS nix neues")
#     print("Differenz:", sensor_G.wertL - sensor_R.wertL, "\t",sensor_G.wertL, sensor_R.wertL )
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

    GruenL = aufGruen(LINKS)
    GruenR = aufGruen(RECHTS)
    if taster.getTotalValue()[2] > 0: # bei betätigung der Taster
        display.leereDisplay()
        display.schreibe("Dooooohseh")
        dose.run()              # Dose umfahren
        Off()
        display.leereDisplay()
        display.schreibe("main")
    diff = sensor_W.wertL - sensor_W.wertR # Differenz bilden
    Adiff = sensor_A.wertL - sensor_A.wertR

    diff = diff*2 # die Differenz mal 2, um den Bewegungsfaktor zu erhöhen
    
    if sensor_A.wertL - sensor_A.wertR > 50:
        diff = 500
        OnFwd(MOT_A,   diff)
        OnFwd(MOT_B,  -diff)
    elif sensor_A.wertR - sensor_A.wertL > 50:
        diff = -500
        OnFwd(MOT_A,   diff)
        OnFwd(MOT_B,  -diff)
    else:
        OnFwd(MOT_B,V - (diff + Adiff) /2) # Geschwindigkeit wird auf verschidene Werte gesetzt
        OnFwd(MOT_A,V + (diff + Adiff) /2)

def intersectionHandler(linksGruen, rechtsGruen):
    Off()
    if linksGruen:
        if rechtsGruen:
            print("Wenn moeglich bitte wenden.")
        else:
            print("In 300 Metern bitte links abbiegen.")
    elif rechtsGruen:
        print("In 300 Metern bitte rechts abbiegen.")
    else:
        print("Dem Strassenverlauf bitte folgen.")
        

    
    
    
    
   
    