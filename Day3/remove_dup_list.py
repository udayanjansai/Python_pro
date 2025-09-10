def rem(li):
    vi=[]
    for i in li:
        if i not in vi:
            vi.append(i)
    return vi
li=list(map(int,input().split()))
li=rem(li)
print(li)