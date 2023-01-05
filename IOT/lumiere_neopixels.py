NBPIXELS=4

from neopixel import NeoPixel
from machine import Pin,ADC
from time import sleep_ms

np = NeoPixel(Pin(14), NBPIXELS)
adc = ADC(0)

LUMIERE_MIN = 300
    

while True:
    valeur=adc.read()
    LED=LUMIERE_MIN-valeur
    if valeur>LUMIERE_MIN:
        for i in range(0,4):
            np[i]=(0,0,LED)
            np.write()  
    else:
        for n in range(0,4):
            np[n]=(0,0,0)
            np.write()
        