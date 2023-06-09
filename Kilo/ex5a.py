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

# 12
# Try this:

# print("Hello"*3)

############################################################################################################################################################################################################

# 13
# Modify the previous example to ask the user how many "Hello"s to print.
# {} does not work, need to use () outside of str

# num = int(input('How many times would you like to say "Hello": \n'))
# print(f'Hello' * (num))

############################################################################################################################################################################################################

# 14
## (challenge question; can skip)
# Construct the following pattern using a `for` loop. Let the user specify how many rows to print.
# A
# AA
# AAA
# AAAA

# for i in range(1,5):
#     print('A' * (i))

############################################################################################################################################################################################################

# 15
# Try this.

# temps_in_F = [90, 47, 16, 82, 68, 100, 30, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")

############################################################################################################################################################################################################

# 15b
# Try this.

# temps_in_F = [90, 47, 16, 82, 68, 100, 30, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")
#     if temp > 90:
#         print("That's hot.")


############################################################################################################################################################################################################

# 16
# Modify the previous question to display the temperature and display whether it is above or below freezing.

# temps_in_F = [90, 47, 16, 82, 68, 100, 30, 25, 40]
# for temp in temps_in_F:
#     print(f"The temperature was {temp}")
#     if temp > 32:
#         print("That's above freezing\n")
#     elif temp < 32:
#         print("That's below freezing\n")
#     else:
#         print("That is freezing\n")

############################################################################################################################################################################################################

# 17
# Try this:

# x = input("Say a word: ")
# if x.endswith("s"):
#     print("That ends with an 's', so it might be plural.")
# print("That's all I have to say.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

# 18
# Modify the previous example so that if the user input ends with "day",
# then the computer will display "I think that's a day of the week."

# x = input("Say a word: ")
# if x.endswith("s"):
#     print("That ends with an 's', so it might be plural.")
# elif x.endswith("day"):
#     print("I think that's a day of the week.")
# else:
#     print("That's all I have to say.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

# 19
# Try this:

# fruits = ["strawberry", "raspberry", "blueberry", "grape", "mango", "melon"]
# count = 0

# for fr in fruits:
#     if fr.endswith("berry"):
#         count += 1

# print("I've finished counting the fruits.")
# print(f"There were {count} that ended with berry.")


########################################################################################################################################################################################################################################################################################################################################################################################################################

# 20
# Using `startswith` (which works quite similarly to endswith),
# count how many of the fruits start with 'm'.
# Then display the count.

# fruits = ["strawberry", "raspberry", "blueberry", "grape", "mango", "melon"]
# count = 0

# for fr in fruits:
#     if fr.startswith("m"):
#         count += 1

# print("I've finished counting the fruits.")
# print(f"There were {count} that starts with 'm'.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

# 21
# Given this list, count how many temperatures are above freezing.
# Display the count.

# temps_in_F = [90, 47, 82, 68, 100, 30, 25, 40]
# count = 0

# for temp in temps_in_F:
#     if temp > 32:
#         count += 1

# print(f'There are {count} temps above freezing.')


########################################################################################################################################################################################################################################################################################################################################################################################################################

# 22
# Copy and modify the previous example to show the user how many
# temperatures are above freezing and how many are below freezing.

# temps_in_F = [90, 47, 82, 68, 100, 30, 25, 40]
# above = 0
# below = 0
# freezing = 0

# for temp in temps_in_F:
#     if temp > 32:
#         above += 1
#     elif temp < 32:
#         below += 1
#     else:
#         freezing += 1

# print(f'There are {above} temps above freezing.')
# print(f'There are {below} temps below freezing.')
# print(f'There are {freezing} temps at freezing.')

########################################################################################################################################################################################################################################################################################################################################################################################################################

# 22b
# Try this.
# Introduction to enumerate

# names = ["Sam", "Lisa", "Micah", "Dave"]
# for indx, elem in enumerate(names):
#     print(f"The index is {indx} and the element is {elem}")

########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################

########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################