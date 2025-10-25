# Task 2: Using the Math Module for Calculations

# 1. Import the math module
import math

# 1. Asks the user for a number as input.
try:
    # Use float() to allow for calculations on both integers and decimals
    number = float(input("Enter a number: "))
    
    # Check for domain errors for math functions (e.g., log of non-positive)
    if number < 0:
        print("\nCalculations for negative numbers are restricted for log and square root.")
        sqrt_result = "Error: Cannot take square root of a negative number"
        log_result = "Error: Cannot take log of a non-positive number"
        # Sine of a negative number is still valid
        sine_result = math.sin(number)
    elif number == 0:
        print("\nCalculations for zero are restricted for log.")
        sqrt_result = math.sqrt(number)
        log_result = "Error: Cannot take log of zero"
        sine_result = math.sin(number)
    else:
        # 2. Uses the math module to calculate the:
        
        # Square root of the number
        sqrt_result = math.sqrt(number)
        
        # Natural logarithm (log base e) of the number
        log_result = math.log(number)
        
        # Sine of the number (in radians)
        sine_result = math.sin(number)

    # 3. Displays the calculated results.
    print("\n--- Results ---")
    print(f"Square root: {sqrt_result}")
    print(f"Logarithm: {log_result}")
    print(f"Sine: {sine_result}")

except ValueError:
    print("Invalid input. Please enter a valid numerical value.")