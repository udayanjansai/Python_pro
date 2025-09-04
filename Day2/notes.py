def notes(n):
    count=0
    while n>0:
        if n>=2000:
            n-=2000
            count+=1
        elif n>=500:
            n-=500
            count+=1
        elif n>=200:
            n-=200
            count+=1
        elif n>=100:
            n-=100
            count+=1
        elif n>=50:
            n-=50
            count+=1
        elif n>=20:
            n-=20
            count+=1
        elif n>=10:
            n-=10
            count+=1
        elif n>=5:
            n-=5
        else:
            n-=1
    return count
n=int(input("enter value "))
print(notes(n))
            