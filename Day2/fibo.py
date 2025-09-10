def fibo(n):
    a=0
    b=1
    print(0,end=' ')
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c,end=' ')
n=int(input("Enter "))
fibo(n)
