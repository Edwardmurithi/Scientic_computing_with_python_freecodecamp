#!/usr/bin/python3
"""
TODO:
	Takes input as plain text
	Gives a cipher as a encryoted text
"""

# Prompt user
plain_text = input("Enter Text: ")
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in plain_text.lower():
    if char == ' ':
        encrypted_text += char # add a space to encrypted text
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet)
        encrypted_text += alphabet[new_index]

print('Plain text:', plain_text)
print('Encrypted text:', encrypted_text)
