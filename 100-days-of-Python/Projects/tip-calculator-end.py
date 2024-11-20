print("Welcome to the tip calculator")
bill=float(input("What was the total bill?\n$"))
tip=int(input("What percentage would you like to give?\n"))
no=int(input("How many people to split the bill?\n"))
total_bill=tip/100*bill+bill
per_person =(round(total_bill / int(no),2))
print(f"Each person should pay ${per_person}")