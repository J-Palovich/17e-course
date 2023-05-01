# Make a copy of your calculator from the earlier PE.
# (The unit conversion portion (KM to m) is not needed here.)
# Save it with a new name.

# In this new version, allow the user to select one of
# the four operations (add, subtract, multiply, divide).
# Only display the result of that one operation.

# Label the result appropriately ("The sum is _" or similar).

# The user must be able to pick any of the four operations
# (add, subtract, multiply, divide).  
# Tell the user what operations are available for selection.

# Notes: 
# 1. For all number inputs, non-whole-number entries must be allowed.
# 2. Use normal division, not "floor division".

# ----------------------

# Rubric:
# 10%  Allows the user to input two numbers
# 20%  Allows the user to input an operation and tells user what operations are availble.
# 10%  Inputs accept non-whole numbers, and these are used in calculations.
# 30%  Displays only the result of the chosen operation
#      (must function correctly for all four
#       available operations)
# 30%  Result is correctly labeled
#      ("The sum is ...", "The product is...", etc 
#       rather than simply displaying the number)

again = 'yes'
print('Hello!')
name = input('What is your name? \n')
print(f"Greetings, {name} \n")

print('This is a basic calculator that adds, subtracts, multiplies, and divides.')
while again.lower() == 'yes':
    num1 = float(input('Please input your first number: \n'))
    num2 = float(input('Please input your second number: \n'))
    operation = input('Would you like to add, subtract, multiply, or divide: ')


    if operation.lower() == 'add':
        print(f'The sum is {num1 + num2}')
    elif operation.lower() == 'subtract':
        print(f'The difference is {num1 - num2}')
    elif operation.lower() == 'multiply':
        print(f'The product is {num1 * num2}')
    elif operation == 'divide':
        print(f'The quotient is {num1 / num2}\n')
    else:
        print("Please enter 'add', 'subtract', 'multiply', or 'divide'.")

    again = input('Would like like to run again? ')
    
print('Have a great day!')