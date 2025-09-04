def sumofdigits(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    print(s)
n=int(input("Enter number: "))
sumofdigits(n)