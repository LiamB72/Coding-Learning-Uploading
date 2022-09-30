lst = []

for x in range(0, 5):
    a = int(input("Choisir un nombre positif. "))
    if a<0:
        lst.append(a)
        break
    lst.append(a)

if min(lst)>=0:
    print('Le nombre le plus petit de votre liste est ', min(lst))
else:
    print('le nombre choisi est negatif, veuillez respecter les regles et reessayer')
