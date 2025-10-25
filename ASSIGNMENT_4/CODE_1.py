# Task 1: Read a File and Handle Errors

FILE_NAME = "sample.txt"

# 1. Opens and reads a text file named sample.txt.
# 3. Handles errors gracefully if the file does not exist.
try:
    print("Reading file content:")
    
    # Use 'with open' for proper file management (automatic closing)
    with open(FILE_NAME, 'r') as file:
        line_number = 1
        
        # 2. Prints its content line by line.
        for line in file:
            # Use .strip() to remove the newline character at the end of each line
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1

except FileNotFoundError:
    # Handles the error if the file specified by FILE_NAME does not exist
    print(f"Error: The file '{FILE_NAME}' was not found.")

except Exception as e:
    # Handles any other potential file reading errors
    print(f"An unexpected error occurred: {e}")