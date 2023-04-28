# print("Here we go!")
# print("If you want \n separate lines, you \n can do it \n like this.")
## 2b
## Try this.
# print("This thing inside quotes is called a \"string\". If you want")
# print("to put quotes inside, this is how.")


#########################################################################################################

## 2c
## Try this.
# print("You have now seen two escape sequences: \n for newline, and \" for a quotation mark.")
# print("Another useful sequence is two backslashes,")
# print("which is used to type a single backslash.")
# print("Example:  \\  will only display one backslash.")


#########################################################################################################

## 2d
## Try this.
# print("""If you put three quote marks, 
# you can easily enter a
# multi-line
# string.""")


#########################################################################################################

## 2e
## You can also use triple quotes similarly to how you use comments:
# """If I wanted to write a long explanation,
# I could write it like this
# instead of using the '#' if I wanted to."""


#########################################################################################################

## 2f
## Try this.
# print('In Python, the single quote can be used instead of the double quote.')

# Variable Exercises
# first = "Bob"
# last = "Smith"
# print(first, last)

## This example uses an f-string. The f stands for "format".
# print(f"My name is {first} {last}")

## (Later, when we get to file writing, the 
## comma approach doesn't work, but f-strings do work.)
# print("My name is", first, last)




#########################################################################################################


# INPUT COMMAND: takes user input to store as variable, much like scanner in java

# print("Hello!")
# carType = input("Say the name of a car, then press enter: ")
# print(f"The car you named is {carType}. That was a good choice.")

# carType2 = input("Say the name of a car, then press enter: ")
# print(f"The car you named is {carType2}. Do you have one?")

# animal = input("Enter the name of an animal: ")
# print(f"The animal you named is {animal}. I think that it would make a nice pet.")

# first = input("What is your first name?\n")
# middle = input("What is your middle name?\n")
# last = input("What is your last name?\n")
# print(f"Your name is {first} {middle} {last}.")

# favColor = input("Hey {first}! What is your favorite color?\n")
# print(f"{favColor} is a pretty color!\n")

# animal = input("Enter the name of a pet:\n")
# plant = input("Now enter the name of a plant:\n")
# print(f"the {animal} eats {plant} every day\n")



#########################################################################################################




#Practice using STRING and Concatiantion
# a = "Hello"
# b = "Goodbye"
# c = a + b
# print(c)

# sentence = "Hello" + " " + "everyone"
# print(sentence)

# a = input("First word?\n")
# b = input("Second word?\n")
# c = a + b
# print(c)

#this does math
# a = 5
# b = 3
# c = a + b
# print(c)

# this does concatenation
# a = "5"
# b = "3"
# c = a + b
# print(c)

#########################################################################################################

# 13 CONCATENATION
# print("Welcome to the number adder that doesn't work right!")
# a = input("What's a number you like? ")
# b = input("Can you give me another number you like? ")
# c = a + b
# print("I added them. Here's what I got...")
# print(c)

#########################################################################################################

## 15
## Try this.  It will perform proper arithmetic. USES INT
# print("Welcome to the number adder that works well!")
# a = int(input("What's a number you like? "))
# b = int(input("Can you give me another number you like? "))
# c = a + b
# print(c)

#########################################################################################################

## 16
## Try this. You will get an error. How do you fix it? (added INT to line 125)
# a = int(input("What is a number you like? "))
# b = int(input("Can you give me another number you like? "))
# c = a + b
# print(c)

#########################################################################################################

## 17
## Try this. You will get an error. How do you fix it? (Again, added INT to line 132)
# favnum = int(input("What is your favorite number? "))
# onemore = favnum + 1
# print(f"One more would be {onemore}")


#########################################################################################################

## 18
## Ask the user for an integer.
## Display "That number plus 2 is ___".
# favnum = int(input("What is your favorite number? "))
# twomore = favnum + 2
# print(f"That number plus 2 is {twomore}")

#########################################################################################################

## 19
## Ask the user for two integers.
## Display "The sum of your two numbers is ___".
# num1 = int(input("Give me a nummy:\n"))
# num2 = int(input("Give me another nummy:\n"))
# print(f"The sum of your nummies is {num1 + num2}")

#########################################################################################################

## 20
## Ask the user for two integers.
## Display "The first number minus the second number is ___".
# num1 = int(input("Give me a nummy:\n"))
# num2 = int(input("Give me another nummy:\n"))
# print(f"The difference of your two nummies is {num1 - num2}")

#########################################################################################################

## 21
## Ask the user for a number.
## Display "Half of that number is ___"
# num1 = int(input("How many cookies do you want?\n"))
# print(f"I stole half your cookies nerd! you now have {num1 / 2} cookies!!")

#########################################################################################################

## 21b
## Try this.
# print("Hello "*3)

#########################################################################################################

## 21bb  (previously #25)
## Copy and modify the previous example to ask the user for a string.
## Display whatever string the user enters three times 
##  (using *3, as in the previous example).
# word = input("Teach the baby a word:\n")
# print(f"The baby yells \"{word * 3}\" at you!")

#########################################################################################################

## 21bbb  (previously #26)
## Copy and modify the previous example to ask the user for both the
## string to be multiplied and the number of repetitions.
# word = input("Teach the baby a word:\n")
# num = int(input("How many tells do you want the baby to say the word?\n"))
# print(f"The baby yells \"{word * num}\" at you!")

#########################################################################################################

## 21c
## Does this example do what you expect?
## If not, how do you fix it? (add INT)
# num = int(input("Give me a number. "))
# print("I'm going to try to multiply that number by 5,")
# print("but something strange is going to happen:")
# print(num*5)

#########################################################################################################

## 22
## Ask the user for the number of questions on a test,
## and ask "how many did you get right?"
## Then, display "You got ___% right". (You'll need to calculate the percent.)
# numQuestions = int(input("How many questions are on the test?\n"))
# numRight = int(input("How many questions did you get right you dumb idiot?\n"))
# score = numRight / numQuestions
# print(f"You scored {score}% nerd")

#########################################################################################################

## 23
## Ask the user for name and age.
## Display "Guess what, ___, in two years you'll be ___."
## (The user-provided name goes in the first blank, and the
##   age two years from now in the second blank.)
# name = input("What is your name homie?\n")
# age = int(input(f"How old are you {name}?"))
# print(f"Guess what Loser!? In two years you'll be {age + 2}")


#########################################################################################################

## 27
## Try this.
## Notice: The type of `x` is integer, and the type of `y` is string.
## The type of 3 is integer.
## What happens when you multiply and integer times an integer?
## What about a string times an integer?
# x = 123
# y = "123"
# print(x*3)
# print(y*3)

#########################################################################################################

## 28
## Try this. It shows how to use the type() function.
## `x` and `y` are both variables, are they integers or strings?
# x = input("Enter a word.")
# y = int(input("Enter a number."))
# print(f"The type of x is {type(x)}, which is another way to say string.")
# print(f"The type of y is {type(y)}, which is another way to say integer.")
# print(x*y)

#########################################################################################################

## 28b
## Determine the type of each of these variables (integer, string, or something else).
## Hint: Python can tell you the types using the type() function.
# mystery = 6
# another = "Hello"
# something = input("Enter a number.")
# whatIsThis = int(input("Enter a number."))
# thisIsSomething = 3.1
# print(f"type of mystery is {type(mystery)}")
# print(f"type of another is {type(another)}")
# print(f"type of something is {type(something)}")
# print(f"type of whatIsThis is {type(whatIsThis)}")
# print(f"type of thisIsSomething is {type(thisIsSomething)}")


#########################################################################################################




#Learning Floats
## Try this. It will give an error. If it doesn't, please ask an instructor.
## 28c 
# Gives error because it uses int() not float()
# somenum = int(input("Try typing a non-whole number, such as an approximate value for pi. You'll see that it doesn't work: "))
# print(f"You typed {somenum}")

#########################################################################################################

# This corrects the error from above
## 28d
## Try this. You'll see that it allows for non-whole numbers.
# somenum = float(input("Try typing another non-whole number: "))
# print(f"You typed {somenum}")

#########################################################################################################

## 28e
## Ask the user for two numbers.
## Use float() in the places where you would use int().
## Display "The sum of your two numbers is ___".
# num1 = float(input("Give me a nummy, any nummy:\n"))
# num2 = float(input("Give me another nummy:\n"))
# print(f"The sums of the two nummies are {num1 + num2}")

#########################################################################################################

## 28f
## Ask the user for a number, making sure that you allow for non-whole numbers.
## Display "Twice that number is ___".
## Example run:
##    Can you give me a number? 3.4
##    Twice that number is 6.8
# num1 = float(input("Give me nummy:\n"))
# print(f"That nummy doubled equals {num1 * 2}")

#########################################################################################################

## 29
## Try this. You will get an error. Why?
## (Note: This isn't fixable. It's a purely educational question.)
# TypeError: can't multiply sequence by non-int of type 'str'
# x = "hello"
# y = "goodbye"
# print(x*y)

#########################################################################################################

## 30
## Try this. You will get an error. Why?
## (Note: no need to try to fix this. It's a purely educational question.)
# This has 3 and 5 as strings not int and gets the same error as before
# x = "3"
# y = "5"
# print(x*y)

#########################################################################################################

## 32
## (Optional)
## You may wonder why you must use the int() function.
## After all, shouldn't the computer know what a number looks like?
## Here's an example of when you WOULDN'T want the number to be an integer.
## (In other words, you want the number to be a string.)

########################################
# This is the right way:
# beg = "800"
# mid = "555"
# end = input("Give me a 4 digit number: ")

# print("Here's an example phone number using the digits you gave me:")
# fullPhoneNum = beg + mid + end
# print(fullPhoneNum)

########################################
# The following version runs, but the output is wrong.
# What's wrong with the output?
# the output does not include beg and mid variables. it adds the number to the input
# beg = 800
# mid = 555
# end = int(input("Give me a 4 digit number: "))

# print("Here's an example phone number using the digits you gave me:")
# fullPhoneNum = beg + mid + end
# print(fullPhoneNum)

########################################
# Another wrong way:
# Why does this fail to run? 
# Changing the input(...) to int(input(...)) is NOT the solution. Why not?
# Is not processed as int
# beg = 800
# mid = 555
# end = input("Give me a 4 digit number: ")

# print("Here's an example phone number using the digits you gave me:")
# fullPhoneNum = beg + mid + end
# print(fullPhoneNum)

