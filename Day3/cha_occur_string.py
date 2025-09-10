def cou(s):
    s=sorted(s)
    vi={}
    for i in s:
        c=0
        for j in s:
            if i==j:
                c+=1
        vi[i]=c
    for i in vi:
        print(i,vi[i],sep='',end='')
def coun(s):
    li=[]
    c=""
    for i in s:
        if i not in li:
            li.append(i)
            c+=i+str(s.count(i))
    print("\n",c)
s=input("Enter ")
cou(s)
coun(s)