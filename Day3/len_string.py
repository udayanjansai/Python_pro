def le(s):
    c=0
    for i in s:
        c+=1
    print("len of s: ",c)
def com(s,s2):
    if s==s2:
        print("both are same")
    else:
        print("not same")
def con(s,s2):
    print("\nconcat ",s+s2)
s=input("Enter string ")
s2=input("Enter s2 ")
le(s)
com(s,s2)
con(s,s2)
