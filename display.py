from ssd1306 import SSD1306_I2C
from meinePins import *
import machine

i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

def schreibe(text,zeile=1,spalte=5):
    oled.text(text,spalte,(zeile-1)*10+8)
    oled.show()
def leereDisplay():
    oled.fill(0)
    oled.show()