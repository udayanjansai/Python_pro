def soffl(n):
    l=n%10
    while n>10:
        n//=10
    f=n
    s=f+l
    print("sum is: ",s)
n=int(input("Enter number: "))
soffl(n)