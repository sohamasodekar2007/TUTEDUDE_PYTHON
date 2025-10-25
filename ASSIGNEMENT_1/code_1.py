# Task 1: Perform Basic Mathematical Operations

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # 2. Performs the basic mathematical operations on these two numbers:

    # Addition
    addition_result = num1 + num2

    # Subtraction
    subtraction_result = num1 - num2

    # Multiplication
    multiplication_result = num1 * num2

    # Division (with basic check for division by zero)
    if num2 != 0:
        division_result = num1 / num2
    else:
        division_result = "Error: Cannot divide by zero"

    # 3. Displays the results of each operation on the screen.
    print("\n--- Results ---")
    print(f"Addition: {addition_result}")
    print(f"Subtraction: {subtraction_result}")
    print(f"Multiplication: {multiplication_result}")
    print(f"Division: {division_result}")

except ValueError:
    print("\nInvalid input. Please enter valid numbers.")