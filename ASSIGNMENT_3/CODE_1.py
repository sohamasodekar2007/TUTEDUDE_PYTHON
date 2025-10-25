# Task 1: Calculate Factorial Using a Function

# 1. Defines a function named factorial
def factorial(n):
    """
    Calculates the factorial of a non-negative integer n using a loop.
    Factorial of 0 is 1. Factorial of n is n * (n-1) * ... * 1.
    """
    # Base case: Factorial of 0 is 1
    if n == 0:
        # 2. Returns the calculated factorial.
        return 1
    
    # Check for negative numbers (Factorial is not defined for negative numbers)
    if n < 0:
        return "Factorial is not defined for negative numbers"

    result = 1
    # Calculates its factorial using a loop
    for i in range(1, n + 1):
        result = result * i
    
    # 2. Returns the calculated factorial.
    return result

# --- Main Program Execution ---

# Get input from the user (ensuring it's an integer)
try:
    num = int(input("Enter a number: "))
    
    # 3. Calls the function with a sample number and prints the output.
    fact_result = factorial(num)
    
    if isinstance(fact_result, int):
        print(f"Factorial of {num} is: {fact_result}")
    else:
        print(fact_result)

except ValueError:
    print("Invalid input. Please enter a whole number.")