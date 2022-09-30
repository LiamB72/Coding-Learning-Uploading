a=int(input("Choose your first number, a="))
b=int(input("Choose your Final number that it bigger than the first one, b="))

while True:
    if b>a:
        if b > 0 or a < 0 and b < 0:
            for x in range(a, b+1, 1):
                print(x)
            break
        elif b < 0:
            for x in range(a, b+1, -1):
                print(x)
            break

    else:
        a=int(input("Choose your first number, a="))
        b=int(input("Choose your Final number that it bigger than the first one, b="))
