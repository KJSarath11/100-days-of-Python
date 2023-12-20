import random
choice=int(input("What do you choose?Type 0 for ROCK, 1 for PAPER and 2 for SCISSOR..1\n"))
computer=random.randint(0,2)
print(f"Computer Chose:\n{computer}")

if(choice==0) and (computer==0):
    print("Draw")
elif(choice == 0) and (computer==1):
    print("computer wins")
elif(choice==0) and (computer==2):
    print("you wins")
elif(choice == 1) and (computer==0):
    print("You win")
elif(choice==1) and (computer==1):
    print("Its Draw")
elif(choice == 1) and (computer==2):
    print("computer wins")
elif(choice==2) and (computer==0):
    print("computer wins")
elif(choice == 2) and (computer==1):
    print("You win")
else:
    print("its a draw")
