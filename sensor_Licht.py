import machine
import utime
import random
from meinePins import *


pinR = machine.ADC(SENSOR_R)
pinL = machine.ADC(SENSOR_L)

class Sensor:
    def __init__(
        self,
        LED,
        name = "TestSensor",
        debug = 0
    ):
        """
        Initialisierung
        """
        #self.pinR = machine.ADC(SENSOR_RECHTS)
        #self.pinL = machine.ADC(SENSOR_LINKS)
        self.led = machine.Pin(LED , machine.Pin.OUT)
        self.wertL = 0
        self.wertR = 0
        self.name = name
        self.maxiL = 0
        self.miniL = 65536
        self.maxiR = 0
        self.miniR = 65536
        
        # init debug
        self.debug = debug
        
    def kalibrierStart(self):
        """
        Reset der Max/Minvariablen
        """
        
        if self.debug == 2:
            print('debug : kalibrierStart')
        
        self.maxiL = 0
        self.miniL = 65536
        self.maxiR = 0
        self.miniR = 65536
        
    def kalibrierRunde(self):
        """
        misst und setzt bei Bedarf Minimum und Maximum
        """
        
        if self.debug == 2:
            print('debug : kalibrierRunde')
        
        self.led.value(1)
        utime.sleep_us(40)
        
        if self.debug == 2:
            print('debug : messe licht')
        
        self.wertR = pinR.read_u16()
        self.wertL = pinL.read_u16()
        #print("messe", self.name)
        
        if self.debug == 2:
            print('debug : set min max')
        
        if self.wertL > self.maxiL:
            self.maxiL = self.wertL
        if self.wertL < self.miniL:
            self.miniL = self.wertL
        if self.wertR > self.maxiR:
            self.maxiR = self.wertR
        if self.wertR < self.miniR:
            self.miniR = self.wertR
        self.led.value(0)

        utime.sleep(0.01)
        if self.debug == 1:
            print('debug : minL = {}, maxiL = {}'.format(
                self.miniL,
                self.maxiL
            ))
            print('debug : minR = {}, maxiR = {}'.format(
                self.miniR,
                self.maxiL
            ))

    def map2int(self, x, in_min, in_max):
        
        output = ((x - in_min) * 100) // (in_max - in_min) 
        
        if self.debug == 2:
            print('debug : map2int-input = {} {} {} '.format(
                x,
                in_min,
                in_max,
            ))
            print('debug : map2int-output = {}'.format(output))
            
        return output 
        
    def messen(self):
        self.led.value(1)
        utime.sleep_us(40)
        if self.debug == 2:
            print('debug : messe licht')
        # messe licht
        WR = pinR.read_u16()
        WL = pinL.read_u16()
        self.led.value(0)
        # map
        
        if self.debug == 2:
            print('debug : messen --> map')
        #self.wertL = WL
        #self.wertR = WR
        
        self.wertL = self.map2int(WL, self.miniL, self.maxiL)
        self.wertR = self.map2int(WR, self.miniR, self.maxiR)
        #print("messe", self.name)
        #print(WL, " > ", self.wertL, " ",WR, " > ", self.wertR)
        
    def setMinMax(self, minL, maxL, minR, maxR):
        self.maxiL = maxL
        self.miniL = minL
        self.maxiR = maxR
        self.miniR = minR
        
        
    def mapTest(self, werte):
        self.map2int(
            werte[0],
            werte[1],
            werte[2],
            werte[3],
            werte[4]
        )
        
# if __name__ == '__main__':
#     
#     werte = [
#         random.randint(0, 65536),
#         0,
#         65536,
#         0,
#         100
#     ]
#     
#     sensorTest = Sensor(LED=20, debug=1)
#     
#     sensorTest.mapTest(werte)
    
    
#twesttzedgtbn bjkh6jfkopgzibhn 4vun 