def triangle(hauteur, largeur):
    for h in range(1,hauteur):
        print("*")
        largeur+=1
        for l in range(1,largeur):
            print("*", end="")
    print("*")

triangle(5,1)