def rem(li,p):
    li=li[:p]+li[p+1:]
    return li
li=list(map(int,input().split()))
p=int(input("Enter pos: "))
li=rem(li,p)
print(li)