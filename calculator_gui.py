import tkinter as tk
from math import sqrt

# Create the main application window
root = tk.Tk()
root.title("Python Calculator")

# Define the global input and result variables
expression = ""
history = []

def update_expression(value):
    global expression
    expression += str(value)
    input_text.set(expression)

def evaluate_expression():
    global expression, history
    try:
        result = str(eval(expression))
        input_text.set(result)
        history.append(expression + " = " + result)
        if len(history) > 5:
            history.pop(0)
        expression = result
    except ZeroDivisionError:
        input_text.set("Error (Division by Zero)")
        expression = ""
    except Exception as e:
        input_text.set("Error")
        expression = ""

def clear_expression():
    global expression
    expression = ""
    input_text.set("")

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    for item in history:
        label = tk.Label(history_window, text=item)
        label.pack()

# Set up the GUI layout
input_text = tk.StringVar()

input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('Arial', 20), bd=10, justify='right')
input_field.grid(row=0, column=0, columnspan=4)

button_frame = tk.Frame(root)
button_frame.pack()

# Add buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('Clear', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('sqrt', 5, 0), ('%', 5, 1), ('^', 5, 2), ('History', 5, 3),
]

for (text, row, col) in buttons:
    action = lambda x=text: update_expression(x) if x != '=' else evaluate_expression()
    if text == 'Clear':
        action = clear_expression
    elif text == 'History':
        action = show_history
    elif text == 'sqrt':
        action = lambda: update_expression('sqrt(')
    elif text == '^':
        action = lambda: update_expression('**')
    tk.Button(button_frame, text=text, width=10, height=2, command=action).grid(row=row, column=col)

root.mainloop()
