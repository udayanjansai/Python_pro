def freq(s):
    s=sorted(s)
    vi={}
    for i in s:
        c=0
        for j in s:
            if i==j:
                c+=1
        vi[i]=c
    print(min(vi,key=vi.get))
def freq2(s):
    vi={}
    for i in s:
        vi[i]=vi.get(i,0)+1
    ma=min(vi,key=vi.get)
    print(ma)
s=input("Enter ")
freq(s)
freq2(s)