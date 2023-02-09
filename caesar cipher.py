alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_amount):
    cipher_text = ""       # taking an empty string          
    for letter in plain_text:   # traversing through the text to encode
       position =  alphabet.index(letter)    # finding position of each letter in alphabet
       new_position = position + shift_amount   # finding new position by increasing shift amount
       new_letter = alphabet[new_position]       # assigning new letter by new position
       cipher_text += new_letter              # concatenating in string
    print(cipher_text)


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position  = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is : {plain_text}")
    
if direction == "encode":
    print(encrypt(plain_text = text, shift_amount = shift))
elif direction == "decode":
    print(decrypt(cipher_text = text,shift_amount = shift))
