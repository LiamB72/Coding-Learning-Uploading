a = 3                                                              #variable for normal number
b = 3.2                                                            #variable for float numbers
c = "le résultat"                                                  #variable for a string
d = a + b# + int(input("what number do you want to add? "))         #int(input("")) make a window popup to put things in it.

tab=[3, 9, 1, 8, 6, 4, 18, 65, 69, 42]                             #creates a list of numbers

print(c, tab[7])                                                   #Tab[0] < it shows the number in place 0 of the list
print(b,"+",a, c, "->",end=" ")                                    #the end="" makes it not return to the next line
print(d)                                                           #returns to the next line
if d == 6.2:
    print("yes")                                                   #although this one isn't affected
else:
    print("no")

#for x in range(12):
#    a += 1
#    print(a, end=", ")

#for y in range(2,8):
#    b = b * 2
#    print(b, end=" ")

a = 36
b = 9
c = a + b
d = a - b
e = a * b
f = a / b
g = a // b
h = a % b
i = a * b
print("c =",c,"d =",d,"e =",e,"f =","g =",g,"h =",h,"i =",i)

a = 2
b = 3
if a == 2 and b == 3: 
print(‘ok’)
else:
print(‘non’)


for n in range(0,5):
print(n,end=’,’)

for n in range(0,11,2):
print(n,end=’,’)

for n in range(6,-1,-1):
print(n,end=’,’)

n=0
while n<5:
print(n,end=’,’)
n=n+1

n=6
while n>=0:
print(n,end=’,’)
n=n-1
