import tkinter

# Create the main window
window = tkinter.Tk()
window.geometry("355x650")
window.title('Calculator')
window.resizable(0, 0)
window.configure(background='black')

# Display area for the calculator
input_entry = tkinter.Entry(window, font=('arial', 30), justify='right', bd=10, insertwidth=4, width=15)
input_entry.grid(row=0, column=0, columnspan=5, pady=(20, 20))

# Initialize row and column values for placing buttons
rowvalue = 1
columnvalue = 0

# List of buttons for the calculator
button_list = ['AC', 'sin', 'cos', 'tan', 'DEL',
               'x\u02b8', '√', '(', ')', '/',
               'ln', '7', '8', '9', 'x',
               'x!', '4', '5', '6', '-',
               'e', '1', '2', '3', '+',
               '1/x', 'π', '0', '.', '=']

# Import the click function from the functions module
from functions import click

# Create buttons and place them in the grid
for i in button_list:
    # Set button color to white for numbers
    bg_color = 'black' if i.isdigit() else 'orange'
    fg_color = 'orange' if i.isdigit() else 'black'

    # Lambda function is used to pass the current button value to the click function
    button = tkinter.Button(window, text=i, command=lambda button=i: click(input_entry, button),
                            height=2, width=3, font=('arial', 20), bg=bg_color, fg=fg_color, activebackground='light blue')
    button.grid(row=rowvalue, column=columnvalue, pady=1)

    # Update row and column values for the next button
    columnvalue += 1
    if columnvalue > 4:
        rowvalue += 1
        columnvalue = 0

# Start the main event loop
window.mainloop()
