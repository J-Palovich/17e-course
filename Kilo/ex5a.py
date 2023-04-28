############################################################################################################################################################################################################

# 1
# Try this:

# colors = ["red", "orange", "yellow"]
# for color in colors:
#     print("Here is a color that I know:")
#     print(color)
    
############################################################################################################################################################################################################

# 2
# Try this:

# names = ["Sam", "Lisa", "Micah", "Dave"]
# for name in names:
#     print(f"Hello {name}. Welcome to the Python course.")

############################################################################################################################################################################################################

# 3
# Copy and modify the previous example like so:
# for each name, display "Have a good day, ____. I hope you enjoyed experimenting with python."
# (Fill in the blank with the name.)

# names = ["Sam", "Lisa", "Micah", "Dave"]
# for name in names:
#     print(f"Have a good day {name}. I hope you enjoyed experimenting with python.")

############################################################################################################################################################################################################
# You can do any operation that you'd like inside of the loop. For example, we could do math on each item in a list:
# 4
# Try this:

# ages = [26, 37, 55, 10, 5]
# for age in ages:
#     print(f"One of the people in my list is {age} years old.")
#     print(f"In two years, that person will be {age + 2} years old.")

############################################################################################################################################################################################################

# 4b
# Copy and modify the previous example so that for each age,
# it displays "5 years ago, that person was ___ years old."

# ages = [26, 37, 55, 10, 5]
# for age in ages:
#     print(f"One of the people in my list is {age} years old.")
#     print(f"In two years, that person will be {age + 2} years old.")
#     print(f"Five years age, that person was {age - 5} years old")


############################################################################################################################################################################################################

# 5
# For each of the following numbers, display “Half of __ is ___”. For example, “Half of 21 is 10.5”
# .0f formats the output

# numbers = [21, 40, 32, 10, 8, 3]
# for num in numbers:
#     print(f"Half of {num} is {num / 2:.0f}.")

###########################################################################################################################################################################################################
# you've seen, you can use a for loop with lists. You can also use a for loop with a string. For example:

# 6
# Try this:

# phrase = "Hello world"
# for letter in phrase:
#     print(f"The letter is {letter}")

############################################################################################################################################################################################################

# 7
# Copy and modify the previous example so it asks the user for a string (rather than only using "Hello world")

# phrase = input('Please enter a phrase:\n')
# for letter in phrase:
#     print(f'{letter}')

############################################################################################################################################################################################################

# 7b
# Copy and modify the previous example so it outputs each letter from the user input followed by "!". For example:
# H!
# e!
# l!git@github.com:J-Palovich/17e-course.git
# l!
# o!
# skips spaces

# phrase = "Hello world"
# for letter in phrase:
#     if letter == ' ':
#         print(f'{letter}')
#     else:
#         print(f"{letter}!")

############################################################################################################################################################################################################
# You can also use a for loop with a range:

# 8
# Try this:

# for num in range(1,5):
#     print(num)

############################################################################################################################################################################################################

# 9
# Modify the previous example to print the numbers 1 to 6.

# for num in range(1,7):
#     print(num)

###########################################git@github.com:J-Palovich/17e-course.git#################################################################################################################################################################

# 10
# For each of the integers 1 to 5, print that number squared.
# Use the range function.
# (In other words, the lists [1, 2, 3, 4, 5] and [1, 4, 9, 16, 25] should not appear in your code.)

# for num in range(1, 6):
#     print(num ** 2)

############################################################################################################################################################################################################

# 11
# Copy and modify the previous example to allow the user to specify the highest number rather than stopping at 5.
# Ex:
# Highest number?  (user types 4)
# 1
# 4
# 9
# 16
# {highNum} does not work, take it out of the bracket

# highNum = int(input('Enter the highest number you would like in range:\n'))
# for num in range(1, highNum):
#     print(num ** 2)

############################################################################################################################################################################################################

# 11b
# (Challenge question)
# Using a nested for-loop, display multiplication facts from 1 to 5:
# 1 * 1 = 1
# 1 * 2 = 2
# ...
# 3 * 4 = 12
# ...
# 5 * 5 = 25

# for num in range(1, 6):
#     print(' ')
#     for i in range(1, 6):
#         print(f'{num} * {i} = {num * i}')

############################################################################################################################################################################################################

# 11c
# Reminder the operator that does remainder in Python?
# Use a for-loop to display the following:
#  1 divided by 4 would have a remainder of ____.
#  2 divided by 4 would have a remainder of ____.
# ...
# 10 divided by 4 would have a remainder of ____.
# 11 divided by 4 would have a remainder of ____.
# 12 divided by 4 would have a remainder of ____.
# Here's a hint. You'll most likely change the a, b, and c.

# for a in range(12):
#     print(f"{a} divided by 4 would have a remainder of {a % 4}")
    
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################