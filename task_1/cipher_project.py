# Define the text to be decrypted
text = 'mrttaqrhknsw ih puggrur'
# Define the custom key for encryption/decryption
custom_key = 'happycoding'

# Vigenère cipher function that can both encrypt and decrypt
def vigenere(message, key, direction=1):
    key_index = 0  # Initialize key index to keep track of position in the key
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Define the alphabet used for the cipher
    final_message = ''  # Initialize the final message as an empty string

    # Loop through each character in the message
    for char in message.lower():

        # If the character is not a letter, add it directly to the final message
        if not char.isalpha():
            final_message += char
        else:
            # Get the current key character, cycling through the key as needed
            key_char = key[key_index % len(key)]
            key_index += 1

            # Calculate the offset based on the key character
            offset = alphabet.index(key_char)
            # Find the index of the current message character in the alphabet
            index = alphabet.find(char)
            # Calculate the new index for the encrypted/decrypted character
            new_index = (index + offset * direction) % len(alphabet)
            # Add the encrypted/decrypted character to the final message
            final_message += alphabet[new_index]

    # Return the final encrypted/decrypted message
    return final_message

# Function to encrypt the message using the Vigenère cipher
def encrypt(message, key):
    return vigenere(message, key)

# Function to decrypt the message using the Vigenère cipher
def decrypt(message, key):
    return vigenere(message, key, -1)

# Print the original encrypted text and the custom key
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
# Decrypt the text using the custom key and print the result
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
