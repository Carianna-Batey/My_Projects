cents=int(input("Please enter a number of cents: "))
quarters=cents//25 #// is floor division, give integer not decimal
cents=cents-quarters*25
dimes=cents//10
cents=cents-dimes*10
nickels=cents//5
cents=cents-nickels*5
pennies=cents//1
print(f"Coins: {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies.")