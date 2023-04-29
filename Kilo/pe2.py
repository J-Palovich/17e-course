# Prompt:
# Ask the user for two integers (base-ten).

# Display each user-provided number in 
# binary, octal, and hexadecimal.
# Label each so the user knows what 
# information is being provided.

# Also, add the same two user-provided numbers, 
# and print the sum in decimal, binary, octal, & hexadecimal. 
# Label each.

# Note 1: In normal math, you can add numbers in binary or in decimal.
# In Python, binary numbers are stored as strings, so you must
# determine whether you should convert to binary before or after
# adding the two numbers.  The same applies to octal & hexadecimal.
# Try some test cases, such as 1 plus 0.

# Note 2: You may display the numbers with or without the prefix,
# based on your preference.
# Example: The number 2 in binary can be displayed as 0b10 or 10.

# ----------------------

# Rubric:
# 15%  Allows the user to input any two integers (base-10).
# 30%  Displays each user-provided number in binary, octal, and hexadecimal
# 15%  Sums are calculated correctly
# 10%  Displays sum of the two input numbers in decimal, binary, octal, and hexadecimal
# 30%  Each output is appropriately labeled to indicate 
#        what it is (the first number, the second number, or the sum),
#        and what number system it is (decimal, binary, octal, or hexadecimal)

############################################################################################################################################################################################################

# Below is the Short-hand answer for the prompt above
# the below code uses a nested for loop that uses indexing to read through the lists
# the for loop runs through every number in numProvided (values in the list of inputs)

# this is believed to be ideal for it is required that every int in the list needs
#    to be ran through

# whereas the second for loop uses indexing to pair the first item in conName and the first
#   item in conAb to be paired and so on for all items in the lists.

# each item in list conName and conAb occurs once per item in numProvided in the respected order

# I realized as I was reviewing the code that using len(conName) and/or 4 for the stop in range
#   would yield the same result, additionally, this only works since the length of
#   conName and conAb are the same length, adding an item to conName will result in an error
#   and adding an item to conAb will result in any additional item greater than the length
#   of conName to be ignored




num1 = int(input('Please enter first integer:\n'))
num2 = int(input('Please enter second integer:\n'))

sum = num1 + num2
numProvided = [num1, num2]
conName = ['decimal', 'binary', 'octal', 'hexadecimal']
conAb = ['d', 'b', 'o', 'x',]

for num in numProvided:
    for i in range(0, len(conName)):
        print(f'{num} in {conName[i]} is: {num:{conAb[i]}}')
    print()

############################################################################################################################################################################################################

# Long-hand answer of for the prompt

# num1 = int(input('Please enter first integer:\n'))
# num2 = int(input('Please enter second integer:\n'))
# sum = num1 + num2

# print(f'{num1} in decimal is: {num1:d}')
# print(f'{num2} in decimal is: {num2:d}\n')

# print(f'{num1} in binary is: {num1:b}')
# print(f'{num2} in binary is: {num2:b}\n')

# print(f'{num1} in octal is: {num1:o}')
# print(f'{num2} in octal is: {num2:o}\n')

# print(f'{num1} in hexadeciaml is: {num1:x}')
# print(f'{num2} in hexidecimal is: {num2:x}\n')

# print(f'The sum of {num1} and {num2} is: {sum}')
# print(f'The sum of {num1} and {num2} in decimal is: {sum:d}')
# print(f'The sum of {num1} and {num2} in binary is: {sum:b}')
# print(f'The sum of {num1} and {num2} in octal is: {sum:o}')
# print(f'The sum of {num1} and {num2} in hexadecimal is: {sum:x}')

############################################################################################################################################################################################################

# EXTRA FAILED LOOP
# for num in numProvided:
#     for name in conName:
#       for i in conAb:
#         print(f'{num} in {name} is: {num:{i}}')
