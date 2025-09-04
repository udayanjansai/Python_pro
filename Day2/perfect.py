def per(n):
    for i in range(1,n):
        j=1
        res=0
        while j<i:
            if i%j==0:
                res+=j
            j+=1
        if res==i:
            print(i,end=' ')
n=int(input("enter "))
per(n)
        