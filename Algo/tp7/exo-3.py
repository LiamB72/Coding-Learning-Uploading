def inversionMot(texte):
    a = ""
    for i in reversed(range(len(texte))):
        a += texte[i]
    return a

texte = str(input("wot?"))
print(inversionMot(texte))