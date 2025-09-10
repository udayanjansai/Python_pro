def count(li):
    c1=c2=0
    for i in li:
        if i%2==0:
            c1+=1
        else:
            c2+=1
    print("no of evens: ",c1,"no of odds: ",c2)
li=list(map(int,input().split()))
count(li)