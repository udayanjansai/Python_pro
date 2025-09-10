
def high(l):
    m=0
    for i in range(len(l)):
        if l[i][2] > 75:
            print(l[i],end=' ')
    print()
def ma(l):
    m=0
    for i in l:
        if i[2]>m:
            m=i[2]
    for i in l:
        if i[2]==m:
            print(i[1])
        
n=int(input("enter: "))
l=[]
for _ in range(n):
    id=int(input("enter number: "))
    name=input("Enter name: ")
    marks=int(input("Enter marks: "))
    t=id,name,marks
    l.append(t)
high(l)
ma(l)