semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
mois=["January"]
mois_lenght = 30
day_count = 0

for i in range(len(mois)):
    for j in range(1,mois_lenght+1):
        for x in range(len(semaine)):
            day_count += 1
            while day_count != 30 and j != 2:
                print(semaine[x], day_count, j, mois[i], end=", ")
            else:
                day_count = 1
                j = 1
        print(end="\n")

