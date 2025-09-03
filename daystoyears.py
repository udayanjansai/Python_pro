days=int(input("Enter days: "))
years=days//365
add=days%365
months=years*12+add//30

print("years: ",years,"months: ",months)
def dayscon(days):
    years=days//365
    add=days%365
    months=years*12+add//30
    print("years: ",years,"months: ",months)