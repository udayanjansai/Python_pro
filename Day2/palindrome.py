def palin(n):
    for i in range(n):
        t=str(i)
        s=t[::-1]
        if t==s:
            print(i,end=' ')
n=int(input("Enter "))
palin(n)
