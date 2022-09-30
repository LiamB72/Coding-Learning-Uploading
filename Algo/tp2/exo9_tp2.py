menu = 0
while menu != 'q':
    print("1 : charger le fichier")
    print ("2 : sauvegarder le fichier")
    print ("3 : afficher les données")
    print ("4 : modifier les données")
    print ("q : quitter")
    menu = input("Votre Choix?")
    if menu == "1":
        print("Chargement")
    elif menu == "2":
        print("Sauvegarde")
    elif menu == "3":
        print("Affichage")
    elif menu == "4":
        print("modification")
    elif menu == 'q':
        print("Au revoir")
    else:
        print("erreur")
