def co(s):
    c1=c2=c3=0
    for i in s:
        if i.isalpha():
            c1+=1
        elif i.isdigit():
            c2+=1
        else:
            c3+=1
    print("no of alpha: ",c1,"no of digits: ",c2,"no of special: ",c3)
s=input("Enter string ")
co(s)