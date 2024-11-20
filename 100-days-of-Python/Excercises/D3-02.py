#BMI 2.0
height=float(input("Enter the height:"))
weight=float(input("Enter the weight:"))
bmi=(weight/height**2)
if bmi<18.5 :
    print(f"Your BMI is {bmi}, you are Under Weight")
elif bmi<25:
    print(f"Your BMI is {bmi}, you are Normal Weight")
elif bmi<30:
    print(f"Your BMI is {bmi}, you are Slightly OverWeight")
elif bmi<35:
    print(f"Your BMI is {bmi}, you are Obese")
else:
    print(f"Your BMI is {bmi}, you are Clinically Obese")
