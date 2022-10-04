from random import *
rep="0"
while rep!="N" and rep!='n':
    nombre = randint(1,5)
    valeur = 0
    coup = 1
    rep="0"
    while valeur != nombre:
        valeur = int(input("Votre Chiffre? "))
        if valeur > nombre:
            print("chiffre trop grand")
            coup += 1
        elif valeur < nombre:
            print("chiffre trop petit")
            coup += 1
        else:
            print("exact, vous l'avez trouvé en",coup,"coup!")
            while rep!="Y" and rep!='y' and rep!="N" and rep!='n':
                rep = input("Voulez vous rejouer? Y/N : ")
                if rep == "N" or rep == 'n':
                    print("au revoir")
