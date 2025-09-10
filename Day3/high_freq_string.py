def freq(s):
    s=sorted(s)
    vi={}
    for i in s:
        c=0
        for j in s:
            if i==j:
                c+=1
        vi[i]=c
    print(max(vi,key=vi.get))
def hi(s):
    vi={}
    for i in s:
        vi[i]=vi.get(i,0)+1
    maxoc=max(vi.values())
    mac=[cha for cha,co in vi.items() if co==maxoc]
    print(mac)
s=input("Enter ")
freq(s)
hi(s)