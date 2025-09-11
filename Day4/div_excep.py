def div(n,d):
    try:
        print(n/d)
    except:
        if ZeroDivisionError:
            print("ERROR division by zero is not allowed\n")
n,m=map(int,input().split())
div(n,m)
