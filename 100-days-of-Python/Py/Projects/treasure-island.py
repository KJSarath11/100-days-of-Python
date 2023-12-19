print("WELCOME TO TREASURE ISLAND\nYour mission is to find the treasure")
choice1=input("Left/Right:\n").lower()
if(choice1=="left"):
    choice2=input("swim/wait:\n").lower()
    if(choice2=="wait"):
        choice3=input("red/blue/yellow:\n").lower()
        if(choice3=="red"):
            print("Congratulations! You found the treasure.")
        elif(choice3=="blue"):
            print("You made a mistake. Try again.")
        elif(choice3=="yellow"):
            print("You're not quick enough. Game over.")
        else:
            print("Wrong door you dead...")
    else:
        print("Caught by a shark...game over")
else:
    print("Fell into hell..game over..")


