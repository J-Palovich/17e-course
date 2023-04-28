# ﻿Display "Hello!"
# Ask the user to input his/her name. 
# Display "Greetings, ___"   (with the user's name in the blank).
# Display "This is a basic calculator that adds, subtracts, multiplies, and divides."
# Ask the user to input the first number. 
# Ask the user to input the second number. 
# Print the following:
#    The sum is __.
#    The difference is __. 
#    The product is __. 
#    The quotient is __.
 
# Display to the user: "Now, we are going to convert km to m."
# Ask the user to input a number of kilometers.
# Display "In meters, that would be __."
# Display "Have a good day!"

# Note: For all number inputs, non-whole-number entries should be allowed.

# Note: Use normal division, not "floor division".

print('Hello!')
name = input('What is your name? \n')
print(f"Greetings, {name} \n")

print('This is a basic calculator that adds, subtracts, multiplies, and divides.')
num1 = float(input('Please input your first number: \n'))
num2 = float(input('Please input your second number: \n'))

print(f'The sum is {num1 + num2}')
print(f'The difference is {num1 - num2}')
print(f'The product is {num1 * num2}')
print(f'The quotient is {num1 / num2}\n')

print('Now we are going to convert km to m')
km = float(input('Please enter a distance in km:\n'))
toMeters = km * 1000
print(f'{km}km in meters would be {toMeters}m\n')

print('Have a great day!')

