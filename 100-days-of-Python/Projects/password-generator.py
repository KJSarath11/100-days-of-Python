import random

letter_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i,' 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G','H',
            'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
            'X', 'Y', 'Z']
number_list=['0','1','2','3','4','5','6','7','8','9']
symbol_list=['!','#','$','%','&','(',')','*','+']


print("WELCOME TO PASSWORD GENERATOR:")
letters=int(input("Enter how many letters you want:\n"))
symbols=int(input("Enter how many symbols you want:\n"))
numbers=int(input("Enter how many numbers you want:\n"))


# #easy method
# password=" "
# for i in range(1,letters+1):
#     password+=random.choice(letter_list)
# for i in range(1,symbols+1):
#     password+=random.choice(symbol_list)
# for i in range(1,numbers+1):
#     password+=random.choice(number_list)

# print(f"Password is:{password}")

#hard method
password=[]
for i in range(1,letters+1):
    password.append(random.choice(letter_list))
for i in range(1,symbols+1):
    password+=(random.choice(symbol_list))
for i in range(1,numbers+1):
    password+=(random.choice(number_list))

print(f"Password is:{password}")
random.shuffle(password)
print(f"Password is:{password}")

final_password=""
for char in password:
    final_password+=char
print(f"Final Password{final_password}")
