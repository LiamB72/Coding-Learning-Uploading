from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def traceDroite(nbDroites,ecart):
    for i in range(nbDroites+1):
	    draw.line((ecart*i,0,ecart*i,hauteur),fill=(0,255,0))

traceDroite(10,20)

img.show()