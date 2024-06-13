#!/usr/bin/python3
"""
This script accepts two numbers and performs the following operations:
Addition, Subtraction, Division, and Multiplication.
"""

# Define the arithmetic functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

# Dictionary to map operation names to functions
operations = {
    'addition': add,
    'subtraction': sub,
    'multiplication': mul,
    'division': div
}

def perform_operation(operation, a, b):
    # Get the function from the dictionary and execute it
    result = operations[operation](a, b)
    return result

def main():
    # Prompt user for two numbers
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    # Perform each operation and print the result
    for operation in operations:
        result = perform_operation(operation, first_number, second_number)
        print(f"{operation.capitalize()}: {first_number} and {second_number} = {result}")

# Ensure the main function is called when the script is executed
if __name__ == '__main__':
    main()
