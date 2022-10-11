def rectangle(hauteur, largeur):
    for h in range(1,hauteur):
        print("*")
        for l in range(1,largeur):
            print("*", end="")
    print("*")

rectangle(7,5)
