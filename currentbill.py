cuno=int(input("Enter customer number: "))
cname=input("Enter customer name: ")
p,l=map(int,input("Enter present and last month bill ").split())
cpu=float(input("Enter cost per unit: "))
totunits=p-l
bill=totunits*cpu
print("Customer no:", cuno, "name:", cname, "present bill:", p, "last month bill:", l)
print("total units:",totunits,"total bill:",bill)