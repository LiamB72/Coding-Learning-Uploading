#exo 4
valeur_tva = 20

prix_ht = 40
tva = prix_ht*valeur_tva/100;
prix_ttc = prix_ht+tva;

print("Prix HT du produit: ",prix_ht," €")
print("Indice de la TVA en 2015: ",valeur_tva," %")
print("Valeur de la TVA: ",tva," €")
print("Prix TTC: ",prix_ttc," €")
