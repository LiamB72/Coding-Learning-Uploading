from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(255,255,255))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def rectangle(x,y,largeur,hauteur,couleur):
    draw.rectangle((x,y,x+largeur, y+hauteur),fill=couleur)

def traceEffetVisuel():
    for i in range(0,largeur+1,16):
        for j in range(0,hauteur+1,16):
            rectangle(i,j,8,8,(2,2,2))



traceEffetVisuel()
img.show()
img.save("effet.png")