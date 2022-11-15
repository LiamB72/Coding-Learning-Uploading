from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=couleur)

def tracecible():
    cercle(128,128,75,(0,0,255))
    cercle(128,128,50,(255,0,0))
    cercle(128,128,25,(255,255,0))

tracecible()
img.show()