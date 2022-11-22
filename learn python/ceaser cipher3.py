alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26

def ceaser(start_txt, shift_amount, cipher_direction):
    end_txt = ' '
    # to get index of each letter in text
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_txt:
        position = alphabet.index(letter)

        new_position = position + shift_amount
        end_txt += alphabet[new_position]
    print(f'The {cipher_direction}d text is {end_txt}')


ceaser(start_txt=text, shift_amount=shift, cipher_direction=direction)
