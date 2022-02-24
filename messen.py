from sensor import *
from taster import *

sensor_R = Sensor(LED_R, "Rot")
sensor_W = Sensor(LED_W, "Weiss")
sensor_G = Sensor(LED_G, "Gruen")

sensoren = [sensor_W, sensor_G, sensor_R]
def ledTest():
    for i in range(4):
        for s in sensoren:
            s.led.on()
            utime.sleep(0.1)
            s.led.off()
            utime.sleep(0.5)
        
def tasterTest():
    while not tasterL.value():
        utime.sleep(0.1)
    sensor_R.led.on()
    utime.sleep(1)
    sensor_R.led.off()
    while not tasterR.value():
        utime.sleep(0.1)
    sensor_R.led.on()
    utime.sleep(1)
    sensor_R.led.off()
    
    

def kalibrieren(anzahl=1000):
    for i in range(anzahl):
        for s in sensoren:
            s.kalibrierRunde()
        utime.sleep(0.01)
    for s in sensoren:
        s.kalibriert=True
    schreibeKalWerte()
        
def schreibeKalWerte():
    f=open(DATEI,"w")
    text=""
    for s in sensoren:
        text=text+str(s.minL)+"\n"
        text=text+str(s.minR)+"\n"
        text=text+str(s.maxL)+"\n"
        text=text+str(s.maxR)+"\n"
    f.write(text)
    #print(text)
    f.close()
    
def liesKalWerte():
    f=open(DATEI,"r")
    text=f.read()
    liste=text.strip().split()
    anzahl= len(sensoren)
    for i in range(anzahl):
        sensoren[i].minL = int(liste[4*i ])
        sensoren[i].minR = int(liste[4*i +1])
        sensoren[i].maxL = int(liste[4*i +2])
        sensoren[i].maxR = int(liste[4*i +3])                  
    f.close()
    for s in sensoren:
        s.kalibriert=True

def zeigeMinMax():
    text=""
    for s in sensoren:
        text=text+s.name+"\n"        
        text=text+"minLi:"+str(s.minL)+"\n"
        text=text+"minRe:"+str(s.minR)+"\n"
        text=text+"maxLi:"+str(s.maxL)+"\n"
        text=text+"maxRe:"+str(s.maxR)+"\n"
    print(text)
def zeigeLichtwerte():
    text=""
    for s in sensoren:
        text=text+s.name+":"+str(s.kalL)+" "+str(s.kalR)+"\n"
    print(text)

def messeLicht():    
    for s in sensoren:
        s.messen()     
        
if __name__=="__main__":
    print("kalibrieren")
    #kalibrieren()
    liesKalWerte()
    zeigeMinMax()    
    while True:
        messeLicht()
        zeigeLichtwerte()
        utime.sleep(0.5)
        