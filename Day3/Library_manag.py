n=int(input("Enter "))
dic={}
for _ in range(n):
    dic.update({int(input("enter id: ")):input("Enter name: ")})
while True:
    c=int(input("Enter 1(add) 2(remove) 3(search) 4(update) 5(dis) 6(count) 7(check)"))
    if c==1:
        dic.update({int(input("Enter id: ")):input("Enter name ")})
    elif c==2:
        dic.pop(int(input("Enter id: ")))
    elif c==3:
        print(dic.get(int(input("enter "))))
    elif c==4:
        k=int(input("Enter "))
        v=input("Enter title ")
        dic[k]=v
    elif c==5:
        print(dic,"\n")
    elif c==6:
        print("no of elem: ",len(dic))
    elif c==7:
        v=input("Enter title: ")
        if v in dic.values():
            print(v," is present")
        else:
            print(v," is not present")
    else:
        break

    
    
 

