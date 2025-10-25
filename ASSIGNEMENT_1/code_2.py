# Problem Statement: Name Concatenation and Greeting

# 1. Takes a user's first name and last name as input.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# 2. Concatenates the first name and last name into a full name.
# A space " " is added between the first and last name.
full_name = first_name + " " + last_name

# 3. Prints a personalized greeting message using the full name.
# Using an f-string for easy formatting.
greeting_message = f"Hello, {full_name}! Welcome to the Python program."

print(greeting_message)