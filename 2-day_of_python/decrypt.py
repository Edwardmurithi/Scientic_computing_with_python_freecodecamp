encrypted_text = input("Enter Encrypted Text: ")
shift = 3

def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plain_text = ''

    for char in encrypted_text.lower():
        if char == ' ':
            plain_text += char
        else:
            index = alphabet.find(char)
            new_index = (index - shift) % len(alphabet)
            plain_text += alphabet[new_index]

    print('Plain Text:', plain_text)
