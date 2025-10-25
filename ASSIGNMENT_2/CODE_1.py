# Task 1: Check if a Number is Even or Odd

# 1. Takes an integer input from the user.
try:
    number = int(input("Enter a number: "))

    # 2. Checks whether the number is even or odd using an if-else statement.
    # A number is even if the remainder when divided by 2 is 0 (number % 2 == 0).
    if number % 2 == 0:
        # 3. Displays the result accordingly.
        print(f"{number} is an even number.")
    else:
        # 3. Displays the result accordingly.
        print(f"{number} is an odd number.")

except ValueError:
    # Handle the case where the user enters non-integer input
    print("Invalid input. Please enter a whole number (integer).")