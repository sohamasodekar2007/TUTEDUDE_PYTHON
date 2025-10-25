# Task 2: Write and Append Data to a File

FILE_NAME = "output.txt"

# 1. Takes user input and writes it to a file named output.txt.
print("--- Step 1: Write to File ---")
try:
    # Get initial input from the user
    initial_text = input(f"Enter text to write to the file: ")
    
    # Use 'w' mode to open the file for writing. This will create the file
    # or overwrite its contents if it already exists.
    with open(FILE_NAME, 'w') as file:
        # Write the text followed by a newline character
        file.write(initial_text + '\n')
    
    print(f"Data successfully written to {FILE_NAME}.")

except IOError:
    print(f"Error: Could not write to the file {FILE_NAME}.")
    # Exit if the initial write fails
    exit()

# 2. Appends additional data to the same file.
print("\n--- Step 2: Append to File ---")
try:
    # Get additional input from the user
    append_text = input(f"Enter additional text to append: ")
    
    # Use 'a' mode to open the file for appending.
    with open(FILE_NAME, 'a') as file:
        # Write the new text followed by a newline character
        file.write(append_text + '\n')
        
    print("Data successfully appended.")

except IOError:
    print(f"Error: Could not append to the file {FILE_NAME}.")

# 3. Reads and displays the final content of the file.
print(f"\n--- Step 3: Read Final Content of {FILE_NAME} ---")
try:
    # Use 'r' mode to open the file for reading.
    with open(FILE_NAME, 'r') as file:
        final_content = file.read()
        
    print(f"Final content of {FILE_NAME}:")
    # Print the entire content read from the file
    print(final_content.strip()) # .strip() removes trailing newlines for clean output

except FileNotFoundError:
    # This block should technically not be reached if the write/append succeeded
    print(f"Error: The file '{FILE_NAME}' was not found (Unexpected).")
except IOError:
    print(f"Error: Could not read from the file {FILE_NAME}.")