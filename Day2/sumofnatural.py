def sumof(n):
    res=0
    while n>0:
        res+=n
        n-=1
    return res
n=int(input("Enter no: "))
print(sumof(n))