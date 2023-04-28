############################################################################################################################################################################################################
## Before starting the exercise, type this at the top of your file:
import random

############################################################################################################################################################################################################

## 1
## Try this.
# things = ["dinosaur", "dog", "cat"]
# print(random.choice(things))

############################################################################################################################################################################################################

## 2
## Make a list of five words of your choice. Print a randomly chosen word.

# words = ["AH", "AHH", "AHHH", "AHHHH", "AHHHHH", "AHHHHHH"]
# print(random.choice(words))

############################################################################################################################################################################################################

## 3
## Make a list of five phrases (instead of single words). Print a randomly chosen phrase.

# phrases = [
#             "Fly me to the moon", "Let me play amoung the stars",
#             "Let me see what spring is like on", "Jupiter and Mars"
#           ]
# print(random.choice(phrases))

############################################################################################################################################################################################################

## 4
## Try this.

# nums = [28, 99, 7]
# oneNum = random.choice(nums)
# print(oneNum)

############################################################################################################################################################################################################

## 5
## Make a list of five numbers.  Print "I randomly picked a number, and I got ____".

# nummies = [1, 2, 3 ,4, 5, 6, 7, 8, 9]
# ranNum = random.choice(nummies)
# print(f'I randomly picked {ranNum}')

############################################################################################################################################################################################################

## 6
## Copy and modify the previous example.
## After displaying the number you picked,
## if the randomly picked number was more than 40, print "It was a big number."
## Otherwise, print "It was not a very big number."

# nummies = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# ranNum = random.choice(nummies)
# print(f'I randomly picked {ranNum}')
# if ranNum > 40:
#     print('That is a large number')
# else:
#     print('That is a fairly small number')

############################################################################################################################################################################################################

## 7
## Try this.
## Does the randomly chosen number include the endpoint?
## (In other words, is it similar to range?)
# Prints a random number between 3 and 6 to include 3 and 6

# num = random.randint(3, 6)
# print(num)

############################################################################################################################################################################################################

## 8
## Make a random score generator using randint.
## Give the user a randomly chosen score: display "You got a ___ on the test".
## (It's up to you how high or low you want your random grades to be.)

# ranNum = random.randint(0, 100)
# print(f'You got a {ranNum} on the Test')

############################################################################################################################################################################################################

## 9 Random Floating Point Number
## Try this.
# x = random.random()  #Generates a radom floating point number from 0.0 to 1.0
# print(x)


############################################################################################################################################################################################################

## 10 Random Floating Point Number of Any Size
## Using the previous example (i.e., x = random.random() ), 
## how could you generate ## a random floating point number of any size?
## Prove your theory in Python.

# i = random.uniform(0, 3)
# print(i)


############################################################################################################################################################################################################

############################################################################################################################################################################################################