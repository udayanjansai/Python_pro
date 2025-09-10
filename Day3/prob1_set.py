def tot(l1,l2,l3):
    s1=set(l1)
    s2=set(l2)
    s3=set(l3)
    tot=len(s1)+len(s2)+len(s3)
    print("tot att: ",tot)
def allthree(l1,l2,l3):
    l=l1+l2+l3
    s=set(l)
    print("attended all 3 days: ",s)
def oneday(l1,l2,l3):
    s1=set(l1)
    s2=set(l2)
    s3=set(l3)
    l=[]
    for i in s1 :
        if i not in s2 and i not in s3:
            l.append(i)
    for j in s2:
        if j not in s2 and j not in s1:
            l.append(j)
    for k in s3:
        if k not in s1 and k not in s2:
            l.append(k)
    print("attend 1: ",l)
def pair(l1,l2,l3):
    s1=set(l1)
    s2=set(l2)
    s3=set(l3)
    l=[]  
    for i in s1:
        if i in s2 and i not in s3:
            l.append(i)   
        elif i in s3 and i not in s2:
            l.append(i)
    for j in s2:
        if j in s1 and j not in s3:
            l.append(j)
        elif j in s3 and j not in s1:
            l.append(j)
    for j in s3:
        if j in s1 and j not in s2:
            l.append(j)
        elif j in s2 and j not in s1:
            l.append(j)
    print("pairs ",l)
l1=input().split()
l2=input().split()
l3=input().split()
tot(l1,l2,l3)
allthree(l1,l2,l3)
oneday(l1,l2,l3)
pair(l1,l2,l3)