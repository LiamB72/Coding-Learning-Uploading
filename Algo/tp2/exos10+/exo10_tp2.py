from random import *
nombre = randint(1,20)
valeur = 0
while valeur != nombre:
    valeur = int(input("Votre Chiffre? "))
    if valeur > nombre:
        print("chiffre trop grand")
    elif valeur < nombre:
        print("chiffre trop petit")
    else:
        print("exact")