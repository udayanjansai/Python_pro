a=10
b=20
print(a,b)
t=a
a=b
b=t
print(a,b)
a,b=b,a
print("after swapping:",a,b)