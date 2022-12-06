semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
mois = ['December','January']
a = 1
for i in range(len(mois)):
    for j in range(5):
        for x in range(len(semaine)):
            print("{0:8}{1:5}{2:2}{3:1}".format(semaine[x], a, " ",mois[i]))
            a += 1
            if a == 32:
                a=1
                break
    print()
