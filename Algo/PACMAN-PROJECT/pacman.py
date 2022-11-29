"""
Program by that's lame
"""
import pygame
from pygame.locals import *
from pygame import mixer

#######################################################################################################################################
#Variables
#######################################################################################################################################

NB_TILES = 27   #nombre de tiles a chager (ici de 00.png à 26.png) 27 au total !!
TITLE_SIZE=32   #definition du dessin (carré)
largeur=25       #hauteur du niveau
hauteur=19       #largeur du niveau
tiles=[]       #liste d'images tiles

pacX=12          #position x y du pacman dans le niveau
pacY=13
compteurBilles=0
life = 3

FRAMERATE_FANTOME= 50      #vitesse du fantome chiffre elevé = vitesse lente
NB_DEPLACEMENT_FANTOME = 7
positionFantome=1
frameRateCounterFantome=0
posfX=24
posfY=18

#######################################################################################################################################
#Level Chart
#######################################################################################################################################
niveau= [[   1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2      ],
        [    6,16,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,16, 6      ],
        [    6,12, 1, 5, 5, 5, 5, 2,12, 1, 5,24,12,23, 5, 2,12, 1, 5, 5, 5, 5, 2,12, 6      ],
        [    6,12, 6, 0, 0, 0, 0, 6,12, 6,12,12,12,12,12, 6,12, 6, 0, 0, 0, 0, 6,12, 6      ],
        [    6,12, 7, 5, 5, 5,10, 4,12, 6,12, 1, 5, 2,12, 6,12, 3,10, 5, 5, 5, 9,12, 6      ],
        [    6,12,25,12,12,12,25,12,12, 6,12, 6, 0, 6,12, 6,12,12,25,12,12,12,25,12, 6      ],
        [    6,12,12,12,26,12,12,12, 1, 9,12, 6, 0, 6,12, 7, 2,12,12,12,26,12,12,12, 6      ],
        [    6,12,23, 5, 8, 5, 5, 5, 8, 4,12, 3, 5, 4,12, 3, 8, 5, 5, 5, 8, 5,24,12, 6      ],
        [    6,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12, 6      ],
        [    3, 5, 5, 5, 5,24,12,12,26,12, 1,24, 0,23, 2,12,26,12,12,23, 5, 5,5,5,4         ],
        [   17,12,12,12,12,12,12,23, 9,12, 6, 0, 0, 0, 6,12, 7,24,12,12,12,12,12,12,18      ],
        [    1, 5, 5, 5, 5,24,12,12,25,12, 6, 0, 0, 0, 6,12,25,12,12,23, 5, 5,5,5,2         ],
        [    6,12,12,12,12,12,12,12,12,12, 3, 5, 5, 5, 4,12,12,12,12,12,12,12,12,12, 6      ],
        [    6,12,23, 5, 5, 5, 5, 2,12,12,12,12,12,12,12,12,12, 1, 5, 5, 5, 5,24,12, 6      ],
        [    6,16,12,12,12,12,12, 6,12,23,24,12,22,12,23,24,12, 6,12,12,12,12,12,16, 6      ],
        [    3, 5, 5, 2,12,26,12, 6,12,12,12,12,12,12,12,12,12, 6,12,26,12, 1, 5, 5, 4      ],
        [    0, 0, 0, 6,12,25,12,25,12, 1, 5, 5, 5, 5, 5, 2,12,25,12,25,12, 6, 0, 0, 0      ],
        [    0, 0, 0, 6,12,12,12,12,12, 6, 0, 0, 0, 0, 0, 6,12,12,12,12,12, 6, 0, 0, 0      ],
        [    0, 0, 0, 3, 5, 5, 5, 5, 5, 4, 0, 0, 0, 0, 0, 3, 5, 5, 5, 5, 5, 4, 0, 0, 0      ]]

fantome=[[   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ]]



"""
[[   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],
        [    0,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12, 0     ],
        [    0,12, 0, 0, 0, 0, 0, 0,12, 0, 0, 0,12, 0, 0, 0,12, 0, 0, 0, 0, 0, 0,12, 0     ],
        [    0,12, 0, 0, 0, 0, 0, 0,12, 0,12,12,12,12,12, 0,12, 0, 0, 0, 0, 0, 0,12, 0     ],
        [    0,12, 0, 0, 0, 0, 0, 0,12, 0,12, 0, 0, 0,12, 0,12, 0, 0, 0, 0, 0, 0,12, 0     ],
        [    0,12, 0,12,12,12, 0,12,12, 0,12, 0, 0, 0,12, 0,12,12, 0,12,12,12, 0,12, 0     ],
        [    0,12,12,12, 0,12,12,12, 0, 0,12, 0, 0, 0,12, 0, 0,12,12,12, 0,12,12,12, 0     ],
        [    0,12, 0, 0, 0, 0, 0, 0, 0, 0,12, 0, 0, 0,12, 0, 0, 0, 0, 0, 0, 0, 0,12, 0     ],
        [    0,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12, 0     ],
        [    0, 0, 0, 0, 0, 0,12,12, 0,12, 0, 0, 0, 0, 0,12, 0,12,12, 0, 0, 0, 0, 0, 0     ],
        [    0,12,12,12,12,12,12, 0, 0,12, 0, 5, 4, 3, 0,12, 0, 0,12,12,12,12,12,12, 0     ],
        [    0, 0, 0, 0, 0, 0,12,12, 0,12, 0, 6, 1, 2, 0,12, 0,12,12, 0, 0, 0, 0, 0, 0     ],
        [    0,12,12,12,12,12,12,12,12,12, 0, 0, 0, 0, 0,12,12,12,12,12,12,12,12,12, 0     ],
        [    0,12, 0, 0, 0, 0, 0, 0,12,12,12,12,12,12,12,12,12, 0, 0, 0, 0, 0, 0,12, 0     ],
        [    0,12,12,12,12,12,12, 0,12, 0, 0,12, 0,12, 0, 0,12, 0,12,12,12,12,12,12, 0     ],
        [    0, 0, 0, 0,12, 0,12, 0,12,12,12,12,12,12,12,12,12, 0,12, 0,12, 0, 0, 0, 0     ],
        [    0, 0, 0, 0,12, 0,12, 0,12, 0, 0, 0, 0, 0, 0, 0,12, 0,12, 0,12, 0, 0, 0, 0     ],
        [    0, 0, 0, 0,12,12,12,12,12, 0, 0, 0, 0, 0, 0, 0,12,12,12,12,12, 0, 0, 0, 0     ],
        [    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ]]
"""


#la taille de la fenetre dépend de la largeur et de la hauteur du niveau
#on rajoute une rangée de 32 pixels en bas de la fentre pour afficher le score d'ou (hauteur +1)
pygame.init()
fenetre = pygame.display.set_mode((largeur*TITLE_SIZE, (hauteur+1)*TITLE_SIZE))
pygame.display.set_caption("Pac-Man")
font = pygame.font.Font('freesansbold.ttf', 20)
#######################################################################################################################################
#Loading Settings
#######################################################################################################################################
def chargetiles(tiles):
    """
    fonction permettant de charger les images tiles dans une liste tiles[]
    """
    for n in range(0,NB_TILES):
        #print('data/'+str(n)+'.png')
        tiles.append(pygame.image.load('data/'+str(n)+'.png')) #attention au chemin


def afficheNiveau(niveau):
    """
    affiche le niveau a partir de la liste a deux dimensions niveau[][]
    """
    for y in range(hauteur):
        for x in range(largeur):
            fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))


def affichePac(numero):
    """
    affiche le pacman en position pacX et pacY
    """
    fenetre.blit(tiles[numero],(pacX * TITLE_SIZE,pacY * TITLE_SIZE))

def afficheScore(score):
    """
    affiche le score
    """
    scoreAafficher = font.render(str(score), True, (255, 255, 255))
    fenetre.blit(scoreAafficher,(390,575))

def afficheVie(life):
    """
    affiche la vie
    """
    text1=('Vie:',life)
    if life == 3:
        VieAafficher = font.render(str(text1), True, (0, 255, 0))
    elif life == 2:
        VieAafficher = font.render(str(text1), True, (255, 255, 0))
    elif life == 1:
        VieAafficher = font.render(str(text1), True, (255, 0, 0))
    fenetre.blit(VieAafficher,(13,575))
#######################################################################################################################################
#Ghost Movement-2 Settings
#######################################################################################################################################
def rechercheFantome(fantome,position): #recherche les coord du fantome dans la liste fantome
    """
    recherche les coordonnées du fantome en fonction du numéro de sa postion dans le parcours
    print(position)
    """                     #la position doit etre dans la liste fantome sinon plantage
    for y in range(hauteur):
        for x in range(largeur):
            if fantome[y][x]==position:
                coodFantome=x,y
    return coodFantome          #les coord du fantome x et y sont dans un tuple coodFantome
def deplaceFantome(fantome):
    """
    Incrémente automatiquement le déplacement du fantome, gère sa vitesse et son affichage
    """

    global frameRateCounterFantome
    global positionFantome
    global posfX,posfY
    global pacX
    global pacY
    global life
    if frameRateCounterFantome==FRAMERATE_FANTOME:      #ralenti la viteese du fantome
        posfX,posfY=rechercheFantome(fantome,positionFantome)   #deballage du tuple coordonnées du fantome
        positionFantome+=1
        if posfX == pacX and posfY == pacY:
                life-=1
                pacX = 12
                pacY = 13
        if life == 0:
            pygame.quit()
        if positionFantome==NB_DEPLACEMENT_FANTOME:     #un tour est fait donc on passe à la 1ere position
            positionFantome=1
        frameRateCounterFantome=0                       #compteur de vitesse à zero
    fenetre.blit(tiles[15],(posfX * TITLE_SIZE,posfY * TITLE_SIZE)) #affichage du fantome
    frameRateCounterFantome+=1                         #incrémentation du compteur de vitesse


chargetiles(tiles)  #chargement des images
#######################################################################################################################################
#Music Settings
#######################################################################################################################################
mixer.init()
mixer.music.load('data/bg-music.wav')
mixer.music.play()
mixer.music.set_volume(0.2)


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False                    #fermeture de la fenetre (croix rouge)

#######################################################################################################################################
#Keys Settings
#######################################################################################################################################
        elif event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?

            if event.unicode == 'z':    #est-ce la touche UP
                affichePac(21)
                posY = pacY - 1
                posX = pacX
                numeroTile = niveau[posY][posX]       #on regarde le numéro du tile
                print("key_up, tile:",numeroTile,end=' ')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 16):   #si le tile est une bille ou un fond noir alors le déplacement est possible
                    pacY -= 1                               #on monte donc il faut décrémenter pacY
                    print("position:",pacX,pacY)
                else:
                    print("Not possible. position:",pacX,pacY)

            elif event.unicode == 's':  #est-ce la touche DOWN
                affichePac(19)
                posY = pacY + 1
                posX = pacX
                numeroTile = niveau[posY][posX]
                print("key_down, tile:",numeroTile,end=' ')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 16):
                    pacY += 1
                    print("position:",pacX,pacY)
                else:
                    print("Not possible. position:",pacX,pacY)


            elif event.unicode == 'd':  #est-ce la touche RIGHT
                affichePac(14)
                posY = pacY
                posX = pacX + 1
                numeroTile = niveau[posY][posX]       #on regarde le numéro du tile
                print("key_right, tile:",numeroTile,end=' ')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 16 or numeroTile == 17 or numeroTile == 18):   #si le tile est une bille ou un fond noir alors le déplacement est possible
                    pacX += 1                               #on monte donc il faut décrémenter pacY
                    print("position:",pacX,pacY)
                else:
                    print("Not possible. position:",pacX,pacY)

            elif event.unicode == 'q':  #est-ce la touche LEFT
                affichePac(20)
                posY = pacY
                posX = pacX - 1
                numeroTile = niveau[posY][posX]       #on regarde le numéro du tile
                print("key_left, tile:",numeroTile,end=' ')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 16 or numeroTile == 17 or numeroTile == 18):   #si le tile est une bille ou un fond noir alors le déplacement est possible
                    pacX -= 1                               #on monte donc il faut décrémenter pacY
                    print("position:",pacX,pacY)
                else:
                    print("Not possible. position:",pacX,pacY)

            elif event.key == pygame.K_ESCAPE: #touche q pour quitter
                loop = False

#######################################################################################################################################
#Other Settings
#######################################################################################################################################
            if (numeroTile==12):  #si le numero du tile est 12 c'est que l'on est sur une nouvelle bille
                compteurBilles+=1   #alors on incrémente le score
                niveau[posY][posX]=0    #et on efface la bille dans le niveau
            if (numeroTile==16):
                niveau[posY][posX]=0
            elif (numeroTile==17):      #left teleporter goes to the posX = 23 which before my other portal
                pacX = 23
            elif (numeroTile==18):      #right teleporter goes to the posX = 1 which after my other portal
                pacX = 1


    fenetre.fill((0,0,0))   #efface la fenetre
    afficheNiveau(niveau)   #affiche le niveau
    affichePac(14)
    afficheVie(life)
    deplaceFantome(fantome) #mettre un commentaire pour desactiver le déplacement du fantome
    afficheScore(compteurBilles)
    pygame.display.update() #mets à jour la fentre graphique
pygame.quit()
