def atoz():
    i='a'
   
    while i<='z':
        print(i,end='')
        i=chr(ord(i)+1)
atoz()
print()
def atoz2():
    i=''
    c=ord('a')
    while c<=ord('z'):
        i+=chr(c)
        c+=1
    print(i)
atoz2()