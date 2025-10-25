import tkinter as tk
from tkinter import messagebox

# Global variable to hold the current expression
expression = ""

def button_click(item):
    """Handles number and operator button clicks."""
    global expression
    # Append the clicked item to the current expression
    expression = expression + str(item)
    # Update the display
    input_text.set(expression)

def button_clear():
    """Clears the display and the expression."""
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    """Evaluates the expression and displays the result."""
    global expression
    try:
        # Evaluate the expression using Python's built-in eval()
        result = str(eval(expression))
        input_text.set(result)
        # Set the expression to the result so further operations can be chained
        expression = result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
        expression = ""
        input_text.set("")
    except:
        # Handle general errors (e.g., invalid syntax like "++")
        messagebox.showerror("Error", "Invalid Input.")
        expression = ""
        input_text.set("")

# ----------------- GUI Setup -----------------

# 1. Create the main window
root = tk.Tk()
root.title("Tkinter Calculator")
# Set a default minimum size
root.geometry("300x400") 
root.resizable(False, False) # Prevent resizing for cleaner layout

# Variable to hold the text displayed in the input field
input_text = tk.StringVar()

# 2. Create the display (Entry Widget)
input_field = tk.Entry(
    root, 
    textvariable=input_text, 
    font=('arial', 20, 'bold'), 
    bd=10, 
    insertwidth=4, 
    width=14,
    justify='right' # Align text to the right
)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the button layout/labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Set a style for all buttons
btn_style = {
    'fg': 'black', 
    'font': ('arial', 15, 'bold'), 
    'bd': 5, 
    'width': 4, 
    'height': 2
}

# 3. Create and place the buttons using a loop and the grid layout
row_val = 1
col_val = 0
for button in buttons:
    # Special colors for operators and clear
    if button in ('/', '*', '-', '+'):
        color = 'orange'
    elif button == 'C':
        color = 'red'
    elif button == '=':
        color = 'green'
    else:
        color = 'light gray'
        
    btn = tk.Button(
        root, 
        text=button, 
        **btn_style, 
        bg=color
    )
    
    # Assign the correct command based on the button type
    if button == '=':
        btn.config(command=button_equal)
    elif button == 'C':
        btn.config(command=button_clear)
    else:
        # Use a lambda function to pass the button's text as an argument to button_click
        btn.config(command=lambda b=button: button_click(b))
        
    # Place the button in the grid
    btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    
    # Update column and row for the next button
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid weight to make buttons expand nicely
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)

# 4. Run the main loop
root.mainloop()