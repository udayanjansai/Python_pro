def numtoword(n):
    s=str(n)
    i=0
    for i in range(len(s)):
        if s[i]=='0':
            print("zero",end=' ')
        elif s[i]=='1':
            print("one",end=' ')
        elif s[i]=='2':
            print("two",end=' ')
        elif s[i]=='3':
            print("three",end=' ')
        elif s[i]=='4':
            print("four",end=' ')
        elif s[i]=='5':
            print("five",end=' ')
        elif s[i]=='6':
            print("six",end=' ')
        elif s[i]=='7':
            print("seven",end=' ')
        elif s[i]=='8':
            print("eight",end=' ')
        elif s[i]=='9':
            print("nine",end=' ')
n=int(input("enter :"))
numtoword(n)

