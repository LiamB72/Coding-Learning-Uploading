from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(1536,256),(0,0,0))
largeur,hauteur=img.size

for x in range(hauteur):
    for y in range(largeur):
         img.putpixel((y,x),(255-x,0,0))


img.show()
img.save("degradex6.jpg")