def freq(li):
    vis=[]
    for i in li:
        if i not in vis:
            c=0
            for j in li:

                if i==j:
                    c+=1
            print(i,"->",c)
            vis.append(i)
li=list(map(int,input().split()))
freq(li)