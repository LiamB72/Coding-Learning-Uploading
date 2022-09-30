from random import *
nombre = randint(1,20)
valeur = 0
coup = 0
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
