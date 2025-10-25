# Task 2: Demonstrate List Slicing

# 1. Creates a list of numbers from 1 to 10.
# Using the range function and list() constructor for conciseness
original_list = list(range(1, 11))

# Print the original list as per the expected output format
print(f"Original list: {original_list}")

# 2. Extracts the first five elements from the list.
# Slicing syntax: [start:stop]
# [0:5] means start at index 0 and go up to (but not including) index 5.
extracted_list = original_list[0:5]

# Print the extracted list
print(f"Extracted first five elements: {extracted_list}")

# 3. Reverses these extracted elements.
# Slicing syntax for reversal: [start:stop:step]
# [::-1] means start at the end, go to the beginning, with a step of -1.
reversed_list = extracted_list[::-1]

# 4. Prints both the extracted list and the reversed list
print(f"Reversed extracted elements: {reversed_list}")