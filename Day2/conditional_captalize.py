def pre(s,l):
    i=s.find(l)
    return s[:i].lower()+s[i:].upper()
s=input("Enter string: ")
l=input("Enter letter: ")
print(pre(s,l))