def moyenneVersion3(lst):
    minimal = min(lst)
    maximum = max(lst)
    total = sum(lst)/len(lst)
    return minimal,maximum,total

lst=[20,8,9,2,35,49]
print(moyenneVersion3(lst))