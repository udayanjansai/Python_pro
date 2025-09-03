vowels=['a','e','i','o','u']
def vowel(s):
    if s in vowels or s in [v.upper() for v in vowels]:
        print("vowels")
    else:
        print("consonant")
c=input("Enter a character: ")
vowel(c)