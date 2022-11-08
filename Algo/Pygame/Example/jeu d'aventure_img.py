"""
Programme réalisé par nom, prénom, classe
"""
import pygame

#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((640, 360))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)
image1=pygame.image.load("vestibule.jpg")
image2=pygame.image.load("salle-a-manger.jpg")
image3=pygame.image.load("cuisine.jpg")
text1 = font.render("vous vous trouvez dans l'entrer", True, (0, 255, 0))
text2 = font.render("vous vous trouvez dans la salle à manger", True, (0, 255, 0))
text3 = font.render("vous vous trouvez dans la cuisine", True, (255, 0, 255))
text4 = font.render("vous vous trouvez dans le salon", True, (255, 0, 255))
text5 = font.render("vous vous trouvez dans le grenier", True, (255, 0, 255))
text6 = font.render("vous vous trouvez au premier étage", True, (255, 0, 255))
text7 = font.render("Vous vous trouvez dans votre chambre", True, (255, 0, 255))
text8 = font.render("Vous vous trouvez dans la chambre de vos parents", True, (255, 0, 255))
text9 = font.render("Vous vous trouvez dans la salle de bain", True, (255, 0, 255))
text10 = font.render("Vous vous trouvez dans la aux toilettes", True, (255, 0, 255))
text11 = font.render("Vous vous trouvez dans le garage", True, (255, 0, 255))


dansQuellePierceEstLePersonnage=1


def decrireLaPiece(piece):
    if piece==1:
        fenetre.blit(image1,(0,0))  #afficher l'image à la prochaine actualisation
        fenetre.blit(text1,(0,300)) #afficher le texte à la prochaine actualisation
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(0,300))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(0,300))



#la fonction decision ou "machine a état" permettant de se déplacer
#ou non en fonction de la pièce ou l'on se situe
def decision(direction,piece):
    print("Vous désirez allez ",direction)
    memorisePiece=piece
    #N : le personnage désire aller au nord
    if direction=='z':
        if piece==1:
            piece=10
        elif piece==4:
            piece=3
        elif piece==2:
            piece=3
    #S : le personnage désire aller au sud
    elif direction=='s':
        if piece==10:
            piece=1
        elif piece==3:
            piece=4
        elif piece==6:
            piece=9
    #E : le personnage désire aller à l'ouest
    elif direction=='q':
        if piece==1:
            piece=11
        elif piece==4:
            piece=1
        elif piece==2:
            piece=4
        elif piece==8:
            piece=6
        elif piece==6:
            piece=7
    #O : le personnage désire aller à l'est
    elif direction=='d':
        if piece==1:
            piece=4
        elif piece==11:
                piece=1
        elif piece==4:
            piece=2
        elif piece==3:
            piece=2
        elif piece==6:
            piece=8
        elif piece==7:
            piece=6
    #O : le personnage désire aller en haut ou en bas
    elif direction=='a':
        if piece==1:
            piece=6
        elif piece==6:
            piece=5
    elif direction=='e':
        if piece==6:
            piece=1
        elif piece==5:
            piece=6
    if memorisePiece==piece:
        print("Deplacement impossible")
    return piece


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            dansQuellePierceEstLePersonnage=decision(event.unicode,dansQuellePierceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'l': #touche q pour quitter
                loop = False
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()

