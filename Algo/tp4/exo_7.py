def moyenneVersion1(lst):
    total = len(lst)
    somme = sum(lst)
    moy = total/somme
    return moy

lst=[20,8,9,2,35,49]
print(moyenneVersion1(lst))