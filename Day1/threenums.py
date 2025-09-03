def three(a,b,c):
    if (a>b) and (a>c):
        print(a,"is the largest")
    elif (b>a) and (b>c):
        print(b,"is the Largest")
    else:
        print(c,"is the Largest")
a,b,c=map(int,input().split())
three(a,b,c)    
