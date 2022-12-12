def WordNoMatterTheWayItsWrittenCheck(text):
    for i in range(len(text)):
        a = text.endswith(text[i])
        b = text.startswith(text[i])
        if a == b :
            return True
        else :
            return False


text = str(input("Give me a palindrome : "))
print(WordNoMatterTheWayItsWrittenCheck(text))
