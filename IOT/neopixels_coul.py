from neopixel import NeoPixel
from machine import Pin

np = NeoPixel(Pin(14), 4)

for i in range(0,4):
    np[i] = (155, 0, 0)

np.write()