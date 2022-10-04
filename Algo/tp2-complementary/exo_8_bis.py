#Formule des nombre premiers
from sympy.ntheory import isprime

#Choisi d'une liste de nombres premiers à partir des nombres donnés par l'ultilisateur
a = int(input("input your first integer number, a = "))
b = int(input("input your second integer number, b = "))
print("now the list of the prime numbre in the range you gave")

while True:
    if b>a: #Si b est supièreur à a alors
        if b > 0 or a < 0 and b < 0:
            for i in range(a,b+1):
                if isprime(i)==True:
                    print(i)
            break
    else:   #Sinon si b est infièreur à a alors
        a=int(input("input your first integer number, a = "))
        b=int(input("Choose your Final number that it bigger than the first one, b="))
