def co(s):
    v=['a','e','i','o','u']
    c1=c2=0
    for i in s:
        if i in v:
            c1+=1
        else:
            c2+=1
    print("no of vowels: ",c1,"no of conso: ",c2)
s=input("Enter string ")
co(s)