import utime
import machine
from meinePins import *
class Sensor:
    def __init__(self,ledPin,name ="Test", pinL=SENSOR_L,pinR=SENSOR_R):
        self.name=name
        self.pinL = machine.ADC(pinL)
        self.pinR = machine.ADC(pinR)
        self.led   = machine.Pin(ledPin,machine.Pin.OUT)
        self.minL = 65535
        self.minR = 65535
        self.maxL = 0
        self.maxR = 0
        self.wertL = 0
        self.wertR = 0
        self.kalL = 0
        self.kalR = 0
        self.kalibriert=False
        
    def setMinMax(self,minL,minR,maxL,maxR):
        """
        setzt die Kalibrierwerte
        """
        self.minL = minL
        self.minR = minR
        self.maxL = maxL
        self.maxR = maxR
    
    def getMinMax(self):
        #liefert ein Tupel (min, max)
        return self.minL, self.minR ,self.maxL,self.maxR
    
    def kalibrierRunde(self):
        # setzt bei Bedarf Minimum und Maximum
        self.messen()    
        if self.wertL > self.maxL:
            self.maxL = self.wertL
        if self.wertL < self.minL:
            self.minL = self.wertL            
        if self.wertR > self.maxR:
            self.maxR = self.wertR
        if self.wertR < self.minR:
            self.minR = self.wertR
        self.led.off()
        
        
    def messen(self):
        self.led.on()
        utime.sleep_us(2)
        self.wertL=self.pinL.read_u16()
        self.wertR=self.pinR.read_u16()        
        self.led.off()
        if self.kalibriert:
            self.kalL= (self.wertL - self.minL) * 100 // (self.maxL - self.minL)
            self.kalR= (self.wertR - self.minR) * 100 // (self.maxR - self.minR)
    
