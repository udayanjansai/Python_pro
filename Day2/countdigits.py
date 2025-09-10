def count(n):
    s=str(n)
    print(len(s))
n=int(input("Enter number: "))
count(n)
def count2(n):
    c=0
    while n>0:
        n//=10
        c+=1
    print(c)
count2(n)
