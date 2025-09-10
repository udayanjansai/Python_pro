def arm(n):
    for i in range(n):
        res=0
        t=i
        while t>0:
            s=t%10
            res+=s**3
            t//=10
        if res==i:
            print(i,end=' ')
n=int(input("Enter "))
arm(n)