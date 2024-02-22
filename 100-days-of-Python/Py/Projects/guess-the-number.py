#choosing difficult
#setting a random number
#guessing a number
#checking whether choosen number is higher or lower and continue until pass/fail
import random

random_number=random.randint(0,100)
print ("I have thought of a number between 0 to 100.")
print(f"Secret number is {random_number}")

difficulty=input("choose the difficulty: ")
if difficulty=="easy":
    attempts=10
elif difficulty=="hard":#hard
    attempts=5
else:
    print("invalid")

while attempts!=0:
    guess=int(input("The number i choose is: "))
    if guess==random_number:
        print(f"The number have been found and the number is {random_number}")
        break
    elif guess>random_number:
        print("Your guess is too high!")
       # print(f"you have {attempts} left")
    else:
        print("Your guess is too low!")
       # print(f"you have {attempts} left")
    attempts-=1
    print(f"You have {attempts} left")
