def compteLettre(lettre,chaine):
    a = 0
    for i in range(len(chaine)):
        if chaine[i] == 'e':
            a += 1
    return a

print(compteLettre('e','je vais au cinema ce soir'))