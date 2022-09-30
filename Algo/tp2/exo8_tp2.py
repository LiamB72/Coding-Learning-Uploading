valeur = []
a = 0
while a >= 0:
    a = int(input("choose a positive value, a = "))
    valeur.append(a)

last_value = valeur.pop()
print(valeur)
somme = sum(valeur)
print('la somme de toutes les valeurs entrées est ', somme)
