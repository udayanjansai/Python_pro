def check(c):
    if c.isalpha():
        print("Alphabet")
    elif c.isdigit():
        print("Number")
    elif c in "+_)(*&^%$#@!)":
        print("Special character")
c=input("Enter a character: ")
check(c)
