lst = []
a = 0
while a>=0:
    a = int(input("Choisir un nombre positif. "))
    lst.append(a)

lst.pop()
print('le nombre le plus petit de votre liste est ', min(lst))
