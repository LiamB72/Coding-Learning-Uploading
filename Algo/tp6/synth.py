
phrase = "bonjour"
print (phrase[1:4])

chaine = "NE PARLEZ PAS SI FORT !"
print(chaine.lower())
chaine="nsi"
chaine=chaine.upper()
print(chaine)

w = "Washington"
t= "Touchard"
lycee= w+" "+t
print (lycee)
print (len(lycee))

chaine = "Bonjour"
for i in range(0, len(chaine)):
    print(chaine[i], end='')

chaine = "Au revoir"
for c in chaine:
    print(c, end='')

chaine=str(input("votre chaine ?"))
if chaine=='bonjour':
    print('hello')
else:
    print('j\'ai rien compris')

s = "Welcome"
print(s[-1])
print(s[-2])

s = "Welcome"
print(s[:6])
print(s[4:])
print(s[1:-1])

s = "Hello computer"
print(s.endswith("uter"))
print(s.startswith("good"))
print(s.find("comp"))
print(s.rfind("o"))
print(s.count("o"))

chaine = "\r  Bien le bonjour\t \t"
s = chaine.strip()
print(s)


ch = 'A'
print(ord(ch))


valeur=127
print(chr(valeur))

chaine = "10.5"
print(type(chaine))
valeur=float(chaine)
print(type(valeur))
print(valeur)
