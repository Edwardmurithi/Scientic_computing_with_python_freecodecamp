def get_valid_name():
      """User input validation."""
      while True:
            user_name = input("What is your name? ")
            if user_name.strip().isalpha(): # check if input only contain letters.
                  return user_name.title()
            else:
                  print("Invalid name, Please enter only alphabetic characters")

def get_greeting_message(user_name, greeting_choice):
      greetings = {
            1: "Hello, {}!".format(user_name),
            2: "Hi there, {}!".format(user_name),
            3: "Welcome back, {}!".format(user_name)
      }

      return greetings.get(greeting_choice, "Hello, {}!".format(user_name))


def main():
      try:
            # Prompt the user to enter their name
            user_name = get_valid_name()

            # Provide option for greeting message
            print("Choose a greeting message.")
            print("1. Hello")
            print("2. Hi there")
            print("3. Welcome back")
            greeting_choice = int(input("Enter your choice (1-3): "))
            # Generate and print the greeting message
            greeting_message = get_greeting_message(user_name, greeting_choice)
            
            print(greeting_message)
      except ValueError:
            print("Invalid input. Please enter a valid choice.")
            greeting_message = get_greeting_message(user_name, greeting_choice)


if __name__ == "__main__":
      main()
