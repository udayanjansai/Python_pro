def dup(li):
    vis=[]
    c=0
    for i in li:
        if i not in vis:
            vis.append(i)
        else:
            c+=1
    print("no of dups: ",c)
li=list(map(int,input().split()))
dup(li)