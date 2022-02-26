alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from ASCII_ART_resource_file import Caesar_Cipher_logo
print(Caesar_Cipher_logo)

def Caesar(start_text,cipher_direction,shift_amount):

    end_text=""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char) #Read the index in the alphabet list
            if cipher_direction == 'encode':
                new_position = position+shift_amount
                char = alphabet[new_position] #Read new char(letter) from the new index in list
                end_text += char
            if cipher_direction == 'decode':
                new_position = position - shift_amount
                char = alphabet[new_position] #Read new char(letter) from the new index in list
                end_text += char
        else:
            end_text += char

    print(f"The {cipher_direction}d text is {end_text}.")

Continue = True
while Continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  #if the user enters a shift that is greater than the number of letters in the alphabet

    Caesar(start_text=text,cipher_direction=direction,shift_amount=shift)
    result=input("Type 'Yes' if you want to go again. Otherwise, type 'No'. ").lower()

    if result == "no":
        Continue = False
        print("Goodbye")

