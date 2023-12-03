import math
import tkinter

# Function to get the current value displayed on the calculator
def get_value(input_entry):
    value = input_entry.get()
    return value

# Function to set the value displayed on the calculator
def add_value(input_entry, value):
    input_entry.delete(0, tkinter.END)
    input_entry.insert(0, str(value))

# Function to concatenate the current value with a digit or operator
def concat(input_entry, digit):
    current = get_value(input_entry)
    new_value = current + str(digit)
    return new_value

# Function to handle button clicks
def click(input_entry, btn):
    value = get_value(input_entry)

    try:
        # Row 1
        if btn == 'AC':
            result = ''
        elif btn == 'sin':
            result = round(math.sin(math.radians(eval(value))), 11)
        elif btn == 'cos':
            result = round(math.cos(math.radians(eval(value))), 11)
        elif btn == 'tan':
            result = round(math.tan(math.radians(eval(value))), 11)
        elif btn == 'DEL':
            result = value
            if result == 'Error':
                result = ''
            else:
                result = value[0:len(value) - 1]

        # Row 2
        elif btn == 'x\u02b8':
            result = round(eval(concat(input_entry, '**')), 11)
        elif btn == '√':
            result = round(math.sqrt(eval(value)), 11)
        elif btn == '(':
            result = concat(input_entry, '(')
        elif btn == ')':
            result = concat(input_entry, ')')
        elif btn == '/':
            result = concat(input_entry, '/')

        # Row 3
        elif btn == 'ln':
            result = round(math.log2(eval(value)), 11)
        elif btn == '7':
            result = concat(input_entry, 7)
        elif btn == '8':
            result = concat(input_entry, 8)
        elif btn == '9':
            result = concat(input_entry, 9)
        elif btn == 'x':
            result = concat(input_entry, '*')

        # Row 4
        elif btn == 'x!':
            result = math.factorial(eval(value))
        elif btn == '4':
            result = concat(input_entry, 4)
        elif btn == '5':
            result = concat(input_entry, 5)
        elif btn == '6':
            result = concat(input_entry, 6)
        elif btn == '-':
            result = concat(input_entry, '-')

        # Row 5
        elif btn == 'e':
            result = round((math.e), 4)
        elif btn == '1':
            result = concat(input_entry, 1)
        elif btn == '2':
            result = concat(input_entry, 2)
        elif btn == '3':
            result = concat(input_entry, 3)
        elif btn == '+':
            result = concat(input_entry, '+')

        # Row 6
        elif btn == '1/x':
            result = round(1 / eval(value), 11)
        elif btn == 'π':
            result = round((math.pi), 11)
        elif btn == '0':
            result = concat(input_entry, 0)
        elif btn == '.':
            result = concat(input_entry, '.')

        elif btn == '=':
            result = eval(value)

    except:
        result = 'Error'

    # Set the result back to the calculator display
    add_value(input_entry, result)
