alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(s_text, shift_value, cipher_direction):
    e_text = ""
    if cipher_direction == "decode":
            shift_value *= -1
    for i in s_text:
        if i in alphabet:   
            position = alphabet.index(i)
            new_position = position + shift_value
            e_text += alphabet[new_position]
        else:
            e_text += i
    print(f"The {cipher_direction}d text is {e_text}")

while True:
    direction = input("Type 'encode' to Encrypt, type 'decode' to decrypt:\n")
    txt = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(s_text=txt, shift_value=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        print("Goodbye")
        break




# My Code

# def encrypt(txt_text, shift_value):
#     cipher_text = ""
#     for i in txt_text:
#         position = alphabet.index(i)
#         new_position = position + shift_value
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")


# def decrypt(txt_text, shift_value):
#     cipher_text = ""
#     for i in txt_text:
#         position = alphabet.index(i)
#         new_position = position - shift_value
#         cipher_text += alphabet[new_position]
#     print(f"The decoded text is {cipher_text}")

# if direction == 'encode':
#     encrypt(txt_text=txt, shift_value=shift)
# elif direction == 'decode':
#     decrypt(txt_text=txt, shift_value=shift)
# else:
#     print("Make sure you spelled correctly !")
