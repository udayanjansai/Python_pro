def bill(p,l):
    tot=p-l
    bill=0
    if tot<=50:
        bill=tot*3.80
    elif tot>50 and tot<=100:
        bill=(50*3.80+(tot-50)*4.20)
    elif tot>100 and tot<=200:
        bill=(50*3.80+50*4.20+(tot-100)*5.10)
    elif tot>200 and tot<=300:
        bill=(50*3.80+50*4.20+100*5.10+(tot-200)*6.30)
    else:
        bill=(50*3.80+50*4.20+100*5.10+100*6.30+(tot-300)*7.50)
    return bill
p,l=map(int,input().split())
res=bill(p,l)
print(res)