############################################################################################################################################################################################################

## 1
## Try this.

# guess = input("Guess one of my words: ")
# if guess == "water" or guess == "food":
#     print("You were right.")
# else:
#     print("Sorry, not right.")

############################################################################################################################################################################################################

## 2
## Try this. Test it thoroughly.
## (DON'T DO THIS IN REAL CODE. You'll see why.)
# always displays the first print statement WRONG

# guess = input("Guess one of my words: ")
# if guess == "water" or "food":
#     print("You were right.")
# else:
#     print("Sorry, not right.")

############################################################################################################################################################################################################

## 4
## What's wrong with this code?
# There is no condition, therefore 'Hello Robert' alwast prints
# There is no variable signed to the input

# input("What is your name? ")
# if "Bob":
#     print("Hello Robert.")

############################################################################################################################################################################################################

## 5
## What's wrong with this code?
# There is no condition, therefore 'Hello Robert' alwast print

# name = input("What is your name? ")
# if "Bob":
#     print("Hello Robert.")

################################################################################################################################################################################################################


## 6
## What's wrong with this code?

# input("What is your name? ")
# if input == "Bob":
#     print("Hello Robert.")


#########################################################################################################################################################################################################

## 7 
## What's wrong with this code?

# name = print(input("What is your name? "))
# if name == "Bob":
#     print("Hello Robert.")

############################################################################################################################################################################################################

## 8
## What's wrong with this code?
# prints 'none' since no value is assigned to name

# name = input(print("What is your name? "))
# if name == "Bob":
#     print("Hello Robert.")

############################################################################################################################################################################################################

## 8b
## This isn't wrong, but it is certainly confusing.
## You shouldn't do this in real code.
## However, it may help you understand what's wrong with the next few examples.

# name = input("What is your name? ")
# George = "Bob"
# if name == George:
#     print("This will print if they typed Bob.")
# else:
#     print("This will print for any other name, including the one that starts with a G and ends with eorge.")

############################################################################################################################################################################################################

## 9
## What's wrong with this code?
# # No condition in if statements so both are printed no matter the input

# first = int(input("Give me a number. "))
# operation = input("Do you want to double the number or half it? Say either 'double' or 'half'.")
# double = first * 2
# half = first / 2
# if double:
#     print(f"Ok, double your number is {double}.")
# if half:
#     print(f"Ok, half your number is {half}.")

############################################################################################################################################################################################################

## 10
## What's wrong with this code?
# assigned the variable to the condition statements, need to use '' to make the string

# first = int(input("Give me a number. "))
# operation = input("Do you want to double the number or half it? Say either 'double' or 'half'.\n")
# double = first * 2
# half = first / 2
# if operation == double:
#     print(f"Ok, double your number is {double}.")
# if operation == half:
#     print(f"Ok, half your number is {half}.")

############################################################################################################################################################################################################

## 11
## What's wrong with this code?
# The input is taking in a string and condition is compared to int therefore the condition is never met

# print("You win the game if your age is exactly 99.")
# age = input("How old are you? ")
# if age == 99:
#     print("You win!")
# else:
#     print("You lose.")

############################################################################################################################################################################################################

## 12
## What's wrong with this code?
# The and condition will not be met since it is comparing one input to two different possiblities

# opinion = input("Do you like celery? ")
# if opinion == "yes" or opinion == "Yes":
#     print("Glad you like it.")
# else:
#     print("You don't like it? You should try it again some time.")

############################################################################################################################################################################################################

## 13
## What's wrong with this code? Why does it always assume that
## the user typed 'yes' even if the user types 'no'?
# Can not use boolean operator to compare strings (use .lower() to fix)
# one condition is always met

# response = input("Do you eat? ")
# if not (response == "no" or response == "No"):
#     print("You didn't say no, so I'm assuming that's a yes. I'm glad to hear that you eat.")
# else:
#     print("It looks like you said no. I'm available if you want to talk about your aversion to food.")

############################################################################################################################################################################################################

## 13b
## What's wrong with this code?
# .lower() is a function and requires () to work

# name = input("What is your name? ")
# if name.lower == "bob":
#     print("Hey Bobby!")
# else:
#     print("Hello, good to meet you.")

############################################################################################################################################################################################################

## 14
## What's wrong with this code?
# Does not compare the input

# opinion = input("Do you like celery? ")
# like = ["yes", "Yes", "YES"]
# if like:
#     print("Glad you like it.")
# else:
#     print("You don't like it? You should try it again some time.")

############################################################################################################################################################################################################

## 15
## What's wrong with this code?
# Nothing, I fixed it for you ;)

# opinion = input("Do you like celery? ")
# # like = ["yes", "Yes", "YES"]
# if opinion.lower() == 'yes':
#     print("Glad you like it.")
# else:
#     print("You don't like it? You should try it again some time.")

############################################################################################################################################################################################################

## 16
## What's wrong with this code?
# using 'in' compares the input to an element inside of the list

# opinion = input("Do you like celery? ")
# if opinion in ["yes", "Yes", "YES"]:
#     print("Glad you like it.")
# else:
#     print("You don't like it? You should try it again some time.")

############################################################################################################################################################################################################
############################################################################################################################################################################################################