numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for number in numbers:
    if number % 15 == 0:
        print(f"{number} fizzbuzz")
    elif number % 3 == 0:
        print(f"{number} fizz")
    elif number % 5 == 0:
        print(f"{number} buzz")
    else:
        print(number)