alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Take input message and shift each char by the shift amount
def encrypt(original_text, shift_amount):
    new_messsage = ''
    for char in original_text:
        if char not in alphabet:
            new_messsage += char
        else:
            index_position = alphabet.index(char)
            new_index = index_position + shift_amount
            if new_index > 25:
                while new_index > 25:
                    new_index -= 25
                new_index -= 1

            if new_index < -25:
                while new_index < -25:
                    new_index = new_index + 25

            new_messsage += alphabet[new_index]
        
    
    print(new_messsage)

encrypt(original_text=text, shift_amount=shift)