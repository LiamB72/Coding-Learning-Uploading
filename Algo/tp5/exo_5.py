from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
for x in range(largeur):
    for y in range(hauteur):
         img.putpixel((y,-x),(240-y,255-x,240-y))


img.show()
img.save("degrade_bi.jpg")