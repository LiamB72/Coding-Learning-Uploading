from neopixel import NeoPixel
from machine import Pin

np = NeoPixel(Pin(14), 4)

np[0] = (0, 0, 0)
np[1] = (0, 0, 0) 
np[2] = (0, 0, 0)
np[3] = (0, 0, 0)

np.write()