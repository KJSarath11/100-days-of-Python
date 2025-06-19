#Love Calculator
print("The love calculator is calculating your score")
name1=input("Name1: ")
name2=input("Name2: ")

combine_name=name1+name2
lower_case=combine_name.lower()

t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
first_digit=t+r+u+e

l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")
second_digit=l+o+v+e

score=int(str(first_digit)+str(second_digit))

if(score<=10 ) or (score>=90):
    print(f"Your score is {score} ,you go together like aluvva and mathikarii...")
elif(score>=40) and (score<=50):
    print(f"Your score is {score}, aahh kozhpulaa ingne pokolumm..")
else:
    print(f"Your score is {score},ooh ningde karyam pokkaa...")
