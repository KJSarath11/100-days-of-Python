alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(start_text, shift_amount,cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amount=shift_amount*-1
    for letter in start_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=(position+shift_amount)%26
            end_text+=alphabet[new_position]
        else:
            end_text+=letter
    print(f"Here's the {direction}d result: {end_text}")

should_end=False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

# def encrytion(plain_text,shift_amount):
#     ciphered_text = ""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position=(position+shift_amount)%26
#         ciphered_text+=alphabet[new_position]
#     print(f"The encryted word is: {ciphered_text}")


# def decryption(ciphered_text,shift_amount):
#     plain_text = ""
#     for letter in ciphered_text:
#         position=alphabet.index(letter)
#         new_position=(position-shift_amount)%26
#         plain_text+=alphabet[new_position]
#     print(f"The encryted word is: {plain_text}")


# if direction=="encode":
#     encrytion(plain_text=text,shift_amount=shift)
# elif direction=="decode":
#     decryption(ciphered_text=text,shift_amount=shift)



