"""
Programme réalisé par nom, prénom, classe
"""
#desciption des pièces en fonction du numéro
def decrireLaPiece(piece):
    if piece==1:
        print("vous vous trouvez dans l'entrer")
    elif piece==2:
        print("vous vous trouvez dans la salle à manger")
    elif piece==3:
        print("vous vous trouvez dans la cuisine")
    elif piece==4:
        print("vous vous trouvez dans le salon")
    elif piece==5:
        print("vous vous trouvez dans le grenier")
    elif piece==6:
        print("vous vous trouvez au premier étage")
    elif piece==7:
        print("vous vous trouvez dans votre chambre")
    elif piece==8:
        print("vous vous trouvez dans la chambre de vos parents")
    elif piece==9:
        print("vous vous trouvez dans la salle de bain")
    elif piece==10:
        print("vous vous trouvez aux toilettes")
    elif piece==11:
        print("vous vous trouvez dans le garage")

#la fonction decision ou "machine a état" permettant de se déplacer
#ou non en fonction de la pièce ou l'on se situe
def decision(direction,piece):
    print("Vous désirez allez ",direction)
    memorisePiece=piece
    #N : le personnage désire aller au nord
    if direction=='en avant':
        if piece==1:
            piece=10
        elif piece==4:
            piece=3
        elif piece==2:
            piece=3
    #S : le personnage désire aller au sud
    elif direction=='en arrière':
        if piece==10:
            piece=1
        elif piece==3:
            piece=4
        elif piece==6:
            piece=9
    #E : le personnage désire aller à l'ouest
    elif direction=='à gauche':
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
    elif direction=='à droite':
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
    elif direction=='en haut':
        if piece==1:
            piece=6
        elif piece==6:
            piece=5
    elif direction=='en bas':
        if piece==6:
            piece=1
        elif piece==5:
            piece=6
    if memorisePiece==piece:
        print("Deplacement impossible")
    return piece

#programme principal
dansQuellePierceEstLePersonnage=1   #variable très explicite
menu='0'
while menu!='q':
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    print("------------------------------------------------------------")
    print("Ou désirez-vous aller?")
    print("en avancer : Nord")
    print("en arrière : Sud")
    print("à droite : Est")
    print("à gauche : Ouest")
    print("si à l'entrer : en haut")
    print("si au premier étage : en bas")
    print("q : quitter")
    print("------------------------------------------------------------")
    menu=input("votre choix ?")
    dansQuellePierceEstLePersonnage=decision(menu,dansQuellePierceEstLePersonnage)

print("Au revoir")


