# Program that prompts the user to enter their name and then prints
# a greeting message including their name.
def greet_user():
      # Prompt the user to enter their name
      user_name = input("What is your name? ")

      # Check if the user entered a name
      if user_name.strip() == "":
            print("You didn't enter a name. Please try again.")
            greet_user() # Call the function recursively to prompt again.
      else:
            # Create the greeting message using string formating.
            greetings = "Hello, {}!".format(user_name)
      
            # Print the greeting message.
            print(greetings)

# Call the function to start the program.
greet_user()