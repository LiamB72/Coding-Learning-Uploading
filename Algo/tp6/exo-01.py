def insertionTexte(texte):
    a = ""
    for i in range(len(texte)-1):
        a += texte[i]+'*'
    a += texte[-1]
    return a

texte=str(input("Votre txt? "))
print(insertionTexte(texte))