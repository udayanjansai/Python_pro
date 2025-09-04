import ast
def tup(li):
    ex=[]
    for i in li:
        temp=list(i)
        temp.sort()

        ex.append(tuple(temp))
    return ex
inp=input()
li=ast.literal_eval(inp)
res=tup(li)
print(res)
