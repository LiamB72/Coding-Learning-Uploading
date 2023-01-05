NBPIXELS=4

from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

np = NeoPixel(Pin(14), NBPIXELS)


def defilement(color):
    for i in range(0,4):
        np[i]=color
        np.write()
        sleep_ms(500)
        np[i]=(0,0,0)
        np.write()

while(True):
    defilement((0,15,0))
