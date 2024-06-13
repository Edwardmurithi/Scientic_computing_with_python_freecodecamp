def verify_card_number(card_number):
    # Initialize sum for odd-positioned digits (from the right)
    sum_of_odd_digits = 0
    
    # Reverse the card number to process from right to left
    card_number_reversed = card_number[::-1]
    
    # Extract digits in odd positions (in the reversed order)
    odd_digits = card_number_reversed[::2]

    # Sum the odd-positioned digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Initialize sum for even-positioned digits (from the right)
    sum_of_even_digits = 0
    
    # Extract digits in even positions (in the reversed order)
    even_digits = card_number_reversed[1::2]
    
    # Process and sum the even-positioned digits
    for digit in even_digits:
        # Double the digit
        number = int(digit) * 2
        
        # If the result is 10 or more, sum the digits of the result
        if number >= 10:
            number = (number // 10) + (number % 10)
        
        # Add the processed number to the sum of even-positioned digits
        sum_of_even_digits += number
    
    # Calculate the total sum of processed odd and even digits
    total = sum_of_odd_digits + sum_of_even_digits
    
    # Return True if the total modulo 10 is 0 (valid card number)
    return total % 10 == 0

def main():
    # Example card number with hyphens
    card_number = '4111-1111-4555-1142'
    
    # Create a translation table to remove hyphens and spaces
    card_translation = str.maketrans({'-': '', ' ': ''})
    
    # Translate the card number to remove hyphens and spaces
    translated_card_number = card_number.translate(card_translation)

    # Verify the card number and print the result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Call the main function
main()
