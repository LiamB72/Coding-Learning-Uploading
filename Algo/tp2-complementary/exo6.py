lst = []
a = 0
while a>=0:
    a = int(input("Choisir un nombre positif. "))
    lst.append(a)

lst.pop()
average = sum(lst)/len(lst)

print(average)
