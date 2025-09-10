def add(li,p):
    li.append(p)
    return li
def rem(li,p):
    li.remove(p)
    return li
def sea(li,p):
        if p in li:
            print(p," is available")
        else:
            print(p," not available")
            
def sort(li):
    return li.sort()
def dis(li):
    for i in li:
        print(i,end=' ')
def count(li):
    print("no of pro in cart: ",len(li))
li=[]
while True:
    ch=int(input("Enter 1(add) 2(rem) 3(search) 4(dis) 5(count) 6(sort) 7(clear) 8(exit): "))
    if ch==1:
        li=add(li,input("enter pro to add: "))
    elif ch==2:
        li=rem(li,input("enter pro to remove: "))

    elif ch==3:
        sea(li,input("pro to search: "))
    elif ch==4:
        dis(li)
        print()
    elif ch==5:
        count(li)
    elif ch==6:
        li.sort()
    elif ch==7:
        li.clear()
    else:
        break
