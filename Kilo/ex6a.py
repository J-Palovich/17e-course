########################################################################################################################################################################################################################################################################################################################################################################################################################


# """Excercises 6a while-loops

## 1
## Try this.

# count = 10
# print(f"count is {count}.")
# count += 1
# print(f"I changed count. Now, it's {count}.")
# count -= 2
# print(f"I changed it again. Now, it's {count}.")


###################################################################################################################################################################################

## 2
## Modify the above example so it asks the user for a number.

# count = float(input('Please enter a number:\n'))
# print(f"count is {count}.")
# count += 1
# print(f"I changed count. Now, it's {count}.")
# count -= 2
# print(f"I changed it again. Now, it's {count}.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 3
## Try this.

# count = 3
# print(count)
# count -= 1
# print(count)
# count -= 1
# print(count)
# count -= 1
# print("Reached zero. Proof:")
# print(count)

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 4
## Let's make the previous example less repetitive.
## Try this:

# count = 3
# while count > 0:
#     print(count)
#     count -= 1
# print("Reached zero. Proof:")
# print(count)

# count = 0
# while count > -1:
#     count += 1
#     print(count)


########################################################################################################################################################################################################################################################################################################################################################################################################################

## 5
## Modify the previous example to let the user pick where to start the count

# count = int(input('Enter a number to start count to zero:\n'))
# while count > 0:
#     print(count)
#     count -= 1
# print("Reacheing zero....... Proof:")
# print(count)

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 6
## Modify the previous example to display
## "Launch in 3"
## "Launch in 2"
## "Launch in 1"
## "Liftoff!"

# count = int(input('Enter a number to start count down: \n'))
# while count > 0:
#     print(f"Launch in {count}")
#     count -= 1
# print("Liftoff!")

########################################################################################################################################################################################################################################################################################################################################################################################################################


## 7
## Try this:
# Time delay in seconds...

import time
# print("Start...")
# time.sleep(10)
# print("Done.")


########################################################################################################################################################################################################################################################################################################################################################################################################################

## 8
## Modify the previous example to let the user pick the number of delay seconds.

# delay = int(input('Enter a time delay in seconds: \n'))
# time.sleep(delay)
# print('Zzzz')

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 9
## Modify the earlier "Liftoff" example to add a small delay to make it more fun.
## (It should wait a second after each number is displayed.)

# count = int(input('Enter a number to start count down: \n'))
# while count > 0:
#     time.sleep(1)
#     print(f"Launch in {count}")
#     count -= 1
# print("Liftoff!")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 10
## Try this.
# keepGoing = "yes"
# while keepGoing == "yes":
#     print("Since the variable keepGoing is still 'yes', I am going to keep going.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, you typed something other than 'yes', so I stopped.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 11
## Copy and modify the previous example like so:
## If the user types "y", then keep looping.

# keepGoing = "yes"
# while keepGoing == "yes" or keepGoing == "y":
#     print("Since the variable keepGoing is still 'yes', I am going to keep going.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, you typed something other than 'yes', so I stopped.")


########################################################################################################################################################################################################################################################################################################################################################################################################################

## 12
## Try this:

# keepGoing = "yes"
# while keepGoing.lower() == "yes" or keepGoing.lower()== "y":
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 13
## Copy and modify the previous example like so:
## Continue looping if the user types any of these: "hey", "woo", or "yes".
## Note: I recommend trying the two exercises in the file ex_3b_if_else_common_condition_mistake.py
##       to avoid a common subtle mistake.

# keepGoing = "yes"
# while keepGoing.lower() in ["hey", "woo", "yes", "y"]:
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 14
## Copy and modify the previous example like so:
## If the user types anything other than "no", then keep going.
## (So the user could type "yes", "hi", etc.)

# keepGoing = "yes"
# while keepGoing.lower() != "no":
#     print("Continuing.")
#     keepGoing = input("Do you want me to keep going? ")
# print("Ok, stopping.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 15
## Try this.
## Reminder: the != operator means "Not equal".

# print("Welcome to the word guesser!")
# guess = ""
# secretWord = "water"
# while guess.lower() != secretWord:
#     guess = input("What is your guess? ")
# print("You got it!")


########################################################################################################################################################################################################################################################################################################################################################################################################################

## 16
## Copy and modify the previous example so that each iteration
## of the loop displays "Let me check to determine whether that's right."
# Added the time delay to make it more fun

# print("Welcome to the word guesser!")
# guess = ""
# secretWord = "water"

# while guess.lower() != secretWord:
#     guess = input("What is your guess? ")
#     print(f'Let me check if {guess} is right...\n')

#     if guess.lower() != secretWord:
#         time.sleep(3)
#         print('That is not the word. \n')

# time.sleep(3)
# print("You got it!")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 17
## Copy and modify the previous example so that each 
## iteration of the loop displays "No, try again"
## (but only if the guess was wrong).

# print("Welcome to the word guesser!")
# guess = ""
# secretWord = "water"

# while guess.lower() != secretWord:
#     guess = input("What is your guess? ")
#     print(f'Let me check if {guess} is right...\n')

#     if guess.lower() != secretWord:
#         time.sleep(3)
#         print('That is not the word. \n')

# time.sleep(3)
# print("You got it!")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 18
## Try this.
## Note: we must set `num` to something before the loop starts,
##       so I arbitrarily picked 0.

# print("Welcome to the number doubler.")
# num = 0
# while num != -1:
#     num = int(input("Type a number, or type -1 to quit: "))
#     print(f"Double your num is {num * 2}.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 19
## Copy and modify the previous example so that instead of doubling numbers,
## it calculates the number squared.

# print("Welcome to the number squared tool")
# num = 0
# while num != -1:
#     num = int(input("Type a number, or type -1 to quit: "))
#     print(f"Your num squared {num ** 2}.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 20
## Copy and modify the previous example so that it does not display
## the doubled number if the user enters -1.

# print("Welcome to the number squared tool")
# num = 0
# while num != -1:
#     num = int(input("Type a number, or type -1 to quit: "))
#     if num == -1:
#         break
#     print(f"Your num squared {num ** 2}.")


########################################################################################################################################################################################################################################################################################################################################################################################################################

## 21
## Try this.
## As a reminder, use Ctrl + C to exit a program.
# its a trap

# while 2 + 2 == 4:
#     print("Hi")
# print("Done")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 22
## Try this.
# condition never met, prints 'done'

# while 2 + 2 == 5:
#     print("Hi")
# print("Done")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 23
## Try this.
# condition met with no end

# while 3 > 2:
#     print("Hi")
# print("Done")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 24
## Try this.
# condition met with no end

# while 2 == 2:
#     print("Hi")
# print("Done")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 25
## Try this.
# condition met with no end

# while True == True:
#     print("Hi")
# print("Done")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 26
## Try this. It's a little less obvious.
# while true: is always true
# sets condition with no way to change it

# while True:
#     print("Hi")
# print("Done")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 27
## Make a loop that displays a message of your choice
## repeatedly forever.

# m = input('Input a broadcast:\n')
# while True:
#     print(m)

########################################################################################################################################################################################################################################################################################################################################################################################################################

## Try this.

# while 1 == 1:
#     color = input("What is your favorite color?\n")
#     print(f"Ok, {color} is a nice color.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 29
## Copy and modify the previous example so that in
## every iteration of the loop, it asks the user for the name of an animal,
## and then it displays "The ____ says 'meow'."

# while 1 == 1:
#     a = input("Name an animal\n")
#     print(f"The {a} says 'meow'.")

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 30
## Copy and modify the previous example so that
## it asks for both the name of the animal and what the animal says,
## and then displays "The ___ says '___'."

# while True:
#     a = input("Name an animal\n")
#     s = input(f"What does the {a} say?l\n")
#     print(f"The {a} says '{s}'.")

#######################################################################################################################################################################################################################################################################################################################################################################################################################

## 31
## Copy and modify the previous example so that
## if the animal is "cat" and the sound is "meow",
## it exits the loop.
## The command for exiting the loop is `break`.
## An example of how to use `break` is below.

# a = ''
# s = ''
# while a.lower() != 'cat' and s.lower() != 'meow':
#     a = input("Name an animal\n")
#     s = input(f"What does the {a} say?\n")
#     print(f"The {a} says '{s}'.\n")


########################################################################################################################################################################################################################################################################################################################################################################################################################

## 32
## Try this.

# print("Welcome to another version of the number doubler.")

# while True:
#     try:
#         num = int(input("Type a number, or type -1 to quit: "))
#         if num == -1:
#             break
#         print(f"Double your num is {num * 2}.")
#     except Exception:
#         print('Please enter a valid whole number\n')

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 33
## Make a word guesser:
##  - When the program starts, display "Welcome to the word guesser!"
##  - Ask the user to guess the secret word.
##  - If the user guesses the word correctly, display "You got it!" and exit the loop.
##  - If the user guesses incorrectly, then randomly display one of these replies:
##        "Not yet, try again."
##        "I bet you'll get it, keep trying!"
##        "That's not it."
##        "I appreciate your patience, but you haven't guessed it yet."
##  - The program must loop to allow the user to continue guessing until he/she correctly guesses the secret word.
##  - The program must allow the user to guess the word regardless of capitalization.
##      Recommended: refer back to the exercise that used .lower() .

# print("Welcome to the number squared tool")
# num = 0
# while num != -1:
#     num = int(input("Type a number, or type -1 to quit: "))
#     if num == -1:
#         break
#     print(f"Your num squared {num ** 2}.")
# Think about the order in which things run to insert break in the appropriate location

import random

# print('WELCOME TO THEE JUNGLE!\n')
# guess =''
# secretWord = 'joe borrow'
# wrongReplies = ['Not Quiet', 'Keep Looking', 'Look Harder']

# while guess.lower() != secretWord:
#     guess = input('What might you find in The Jungle?\n')
#     if guess.lower() == secretWord:
#         break
#     print(random.choice(wrongReplies))

# print('WHO DEY!')

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 34
## Make a remainder study tool:
## Have Python pick a random number between 20 and 100.
## Ask the user: "If you divided {the_randomly_chosen_number} by 12, what would be the remainder?"
## Allow the user to guess repeatedly until the user correctly guesses the remainder.
## Example run:
## If you divided 27 by 12, what would be the remainder?
## Guess: 5
## Guess: 2
## Guess: 3
## You got it!

# print('Welcome to Guess The Remainder\n')
# numRan = random.randint(20,101)
# numGuess = -1
# remainder = numRan % 12
# print(f'If you divided {numRan} by 12, what would be the remainder?')

# while numGuess != remainder:
#     numGuess = int(input('Guess: '))
#     if numGuess == remainder:
#         print('You git it!')
#         break

#######################################################################################################################################################################################################################################################################################################################################################################################################################

## 35
## (challenge question)
## {Do this exercise after you've learned to write files.}
## Display "This is a grade tracking helper."
## Open a file named "physics_grades.csv" for writing.
## Write to the file: "StudentName,StudentGrade"
## Ask the user: "What is the total number of questions for this assignment? "
## In a loop:
##    Ask the user: "What is the student name? (Press enter with no name to exit.) "
##    If the user entered nothing, then close the file, display "Exiting..." and exit the loop.
##    If the user entered a name:
##      Ask the user: "How many questions did that student answer correctly? "
##      Compute the percent score for that student.
##      Display the percent, rounded to 2 decimal places.
##      Write to the file: "Bob,92.36%" (but with the actual name and percent instead).
## NOTE: After you have tested your program, try opening the physics_grades.csv file in a spreadsheet program such as Libreoffice Calc.



########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################