def grade(m1,m2,m3):
    if m1>=40 and m2>=40 and m3>=40:
        avg=(m1+m2+m3)//3
        if avg>40 and avg<=50:
            print("C grade")
        elif avg>50 and avg<=70:
            print("B grade")
        elif avg>70 and avg<=80:
            print("A grade")
        else:
            print("Distension")
    else:
        print("Fail")
m1,m2,m3=map(int,input("Enter marks :").split())
grade(m1,m2,m3)