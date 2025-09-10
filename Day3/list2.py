def great(li):
    ma=0
    
    for i in li:
        if i>ma:
            ma=i
    return ma
li=list(map(int,input().split()))
print("max is: ",great(li))

