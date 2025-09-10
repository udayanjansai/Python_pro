def unq(li):
    vis=[]
    for i in li:
        if i not in vis:
            print(i,end=" ")
            vis.append(i)
li=list(map(int,input().split()))
unq(li)