from random import *
rep="0"
while rep!="N":
    nombre = randint(1,20)
    valeur = 0
    coup = 1
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
            while rep!="Y" and rep!="N":
                rep = input("Voulez vous rejouer? Y/N : ")
                if rep == "N":
                    print("au revoir")
