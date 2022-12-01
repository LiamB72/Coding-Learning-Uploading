def fonctionpremierMot(chaine):
    a=""
    for i in range(len(chaine)):
        if chaine[i] != chr(32):
            a += chaine[i]
        else:
            break
    return a



print(fonctionpremierMot("enfin il arrête de pleuvoir "))

