# Task 1: Create a Dictionary of Student Marks

# 1. Creates a dictionary where student names are keys and their marks are values.
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}

# 2. Asks the user to input a student's name.
student_name = input("Enter the student's name: ")

# Safely convert the input to title case for consistent lookup, 
# assuming names in the dictionary are capitalized.
name_to_check = student_name.title()

# Check if the student's name exists in the dictionary
if name_to_check in student_marks:
    # 3. Retrieves and displays the corresponding marks.
    marks = student_marks[name_to_check]
    print(f"{name_to_check}'s marks: {marks}")
else:
    # 4. If the student's name is not found, display an appropriate message.
    print("Student not found.")