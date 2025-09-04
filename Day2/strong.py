def fact(n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)
def strong(n):
    for i in range(n):
        res=0
        t=i
        while t>0:
            s=t%10
            res+=fact(s)
            t//=10
        if res==i:
            print(i,end=' ')
n=int(input("Enter "))
strong(n)
