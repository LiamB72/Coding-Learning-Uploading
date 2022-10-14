m = int(input("votre coef. directeur est : "))
p = int(input("votre ordonnée à l'origine est : "))

while True:
    print("for a range of -10 to 10 :")
    for x in reversed(range(0, -11, -1)):
        print(m*x+p, end=", ")
    for x in range(0, 11):
        print(m*x+p, end=", ")
    break
