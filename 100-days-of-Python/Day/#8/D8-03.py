#prime checker
def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if number % i == 0:
            is_prime=False
    if is_prime:
        print("The number is Prime")
    else:
        print("The number is not Prime")
no=int(input("Enter the number:"))
prime_checker(number=no)


    