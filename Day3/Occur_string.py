def occur(s,c):
    co=0
    for i in s:
        if i==c:
            co+=1
    print("occur of",c,"is: ",co)
s=input("Enter ")
c=input("Enter cha: ")
occur(s,c)
