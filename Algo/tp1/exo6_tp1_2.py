#exo 6
age = int(input("What's your age? your are "))
if age>=6 and age<=7:
    print("Poussin")
else:
    if age>=8 and age<=9:
        print("Pupille")
    else:
        if age>=10 and age<=11:
            print("Minime")
        else:
            if age>=12 and age<=15:
                print("Cadet")
            else:
                if age>15:
                    print("Hors catégorie")
