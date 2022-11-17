from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(1536,256),(0,0,0))
largeur,hauteur=img.size

def traceDroite(nbDroites,ecart):
    for i in range(nbDroites+1):
	    draw.line((ecart*i,0,ecart*i,hauteur),fill=(0,0,0))

for x in range(largeur):
    for y in range(hauteur):
        img.putpixel((x,y),(255,0+x,0))

for x in range(256,largeur):
    for y in range(hauteur):
        img.putpixel((x,y),(255-(x-255),255,0))

for x in range(512,largeur):
    for y in range(hauteur):
        img.putpixel((x,y),(0,255,0+(x-512)))

for x in range(758,largeur):
    for y in range(hauteur):
        img.putpixel((x,y),(0,255-(x-758),255))

for x in range(1014,largeur):
    for y in range(hauteur):
        img.putpixel((x,y),(0+(x-1014),0,255))

for x in range(1270,largeur):
    for y in range(hauteur):
        img.putpixel((x,y),(255,0,255-(x-1270)))
    if x==69420:
        break

img.show()
img.save("degradex6.jpg")