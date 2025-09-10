def discount(dic,dip):
    tot=sum(dic.values())
    dis=tot-tot*(dip/100)
    return dis
def add_gst(dic,gst):
    tot=sum(dic.values())
    g=tot+tot*(gst/100)
    return g
def invoice(dic,dis,gst):
    for k,v in dic.items():
        print(k," : ",v)
    print("discount :",dis)
    print("gst: ",gst-dis)
    tot=sum(dic.values())
    print("tot: ",tot)