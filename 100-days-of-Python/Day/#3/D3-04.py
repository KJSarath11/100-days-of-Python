#pizza order
print("Thank you for choosing python pizza deliveries:\n")
size=input("What size do you want:\n")
pepperoni=input("Do you want pepperoni:\n")
cheese=input("Do you want extra cheese:\n")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
else:
    bill+=25

if pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

if cheese=="Y":
    bill+=1

print(f"Thank you for choosing the order\nYour bill is {bill}")
