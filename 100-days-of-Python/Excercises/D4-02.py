#Banker Roulette
import random
names=["Angela","Ben","Jenny","Michael","Cloe"]
no_of_items=len(names)
selected=random.randint(0,no_of_items-1)
random_choice=names[selected]
print(f"The one paying for the bill is {random_choice}")