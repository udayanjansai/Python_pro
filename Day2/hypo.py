import math
def hypo(a,b):
    res=math.sqrt(a**2+b**2)
    print("hypo: ",res)
    print("hypo ",math.hypot(a,b))
a,b=map(int,input("Enter ").split())
hypo(a,b)


