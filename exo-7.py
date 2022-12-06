voyelles=['a','A','e','E','i','I','o','O','u','U','y','Y']

def compteVoyelles(chaine):
    a=0
    for j in range(len(voyelles)):
        for i in range(len(chaine)):
            if chaine[i] == voyelles[j]:
                a+=1
    return a


chaine=str(input("votre chaine ?"))
print(chaine,compteVoyelles(chaine))