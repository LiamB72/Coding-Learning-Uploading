from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for x in range(largeur):
    for y in range(hauteur):
         img.putpixel((-y,-x),(0,255-y,0))
img.show()
img.save("degrade_green.jpg")