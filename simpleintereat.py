p,t,r=map(int,input().split())
print("simple interest:",(p*t*r)/100)
def interest(p,t,r):
    i=(p*r)/100
    c=0
    while c<t:
        p+=i
        c+=1
    print("Compound interest:",p)
