def compteDesMots(chaine):
    a=1
    for i in range(len(chaine)):
        if chaine[i] == " ":
            a += 1
    return a


chaine=str(input("votre chaine ?"))
print(chaine,compteDesMots(chaine))