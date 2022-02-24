from machine import Pin, PWM
from meinePins import *
import utime

class Motor:
    def __init__(self,in1,in2,pwm):
        self.pwm    = PWM(Pin(pwm))
        self.in1    = Pin(in1,Pin.OUT)
        self.in2    = Pin(in2,Pin.OUT)
        self.pwm.freq(1000)
        
    def aus(self):
        self.pwm.duty_u16(0)
        self.in1.off()
        self.in2.off()
    
    def vor(self,geschw):
        if geschw<0:
            self.back(geschw*(-1))
        else:    
           if geschw>100:
              geschw=100
           self.in1.on()
           self.in2.off()
           self.pwm.duty_u16(650*geschw)
        
    def back(self,geschw):
        if geschw<=0:
            self.aus()
        else:    
            if geschw>100:
                geschw=100
            self.in1.off()
            self.in2.on()
            self.pwm.duty_u16(650*geschw)
        

Mot_A= Motor(A1,A2,PWMA)
Mot_B= Motor(B1,B2,PWMB)

def Off(mot= MOT_AB):
   if mot&MOT_A:
      Mot_A.aus()
   if mot&MOT_B:
      Mot_B.aus()


def OnFwd(mot, speed):
   if speed == 0:
      Off(mot)
   else:   
       iSpeed = int(speed)   
       if mot&MOT_A:
          Mot_A.vor(iSpeed)
       if mot&MOT_B:
          Mot_B.vor(iSpeed)
      
def OnRev(mot,speed):
    OnFwd(mot, -speed)
 