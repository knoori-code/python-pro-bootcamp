alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Take input message and shift each char by the shift amount
def encrypt(original_text, shift_amount):
    encrypted_message = ''
    for char in original_text:
        if char not in alphabet:
            encrypted_message += char
        else:
            original_index = alphabet.index(char)
            new_index = original_index + shift_amount
            new_index = new_index % len(alphabet)
            encrypted_message += alphabet[new_index]

    print(f"The new message is: {encrypted_message}")

def decrypt(original_text, shift_amount):
    decrypted_message = ''
    for char in original_text:
        if char not in alphabet:
            decrypted_message += char
        else:
            original_index = alphabet.index(char)
            new_index = original_index - shift_amount
            new_index = new_index % len(alphabet)
            decrypted_message += alphabet[new_index]

    print(f"The decrypted message is: {decrypted_message}")


def caesar(original_text, shift_amount, direction):
    if direction == "encode":
        encrypt(original_text, shift_amount)
    else:
        decrypt(original_text, shift_amount)

caesar(original_text=text, shift_amount=shift, direction=direction)
        
