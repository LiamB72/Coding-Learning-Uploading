#Formule des nombres premiers
from sympy.ntheory import isprime
for i in range(0,150+1):
    if isprime(i)==True:
        print(i)
