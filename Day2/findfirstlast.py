def fi(n):
    s=str(n)
    f,l=s[0],s[-1]
    print("first: ",f,"last: ",l)
n=int(input())
fi(n)
def fin(n):
    l=n%10
    while n>10:
        n//=10
    f=n
    print("first: ",f,"last: ",l)
fin(n)