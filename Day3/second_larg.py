def sec(li):
    m=0
    m2=0
    for i in li:
        if i >m:
            m=i
    for i in li:
        if i>m2 and i<m:
            m2=i
    print("Second: ",m2)
li=list(map(int,input().split()))
sec(li)
