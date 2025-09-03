stuno=int(input("Enter student number: "))
stuname=input("Enter student name: ")
m1,m2,m3=map(int,input().split())
tot=m1+m2+m3
avg=round(tot/3,2)
print("student no",stuno,"name:",stuname,"marks:",m1,m2,m3)
print("total:",tot,"avg:",avg)