## EXERCISES ------------------------------------------------------------------------
## 1
## Try this. Run it more than once.
# Outputs random number 5 - 8 to include 5 and 8

# import random
# randomNumber = random.randint(5, 8)
# print(f"Here's a random integer: {randomNumber}")

######################################################################################################

## 1b
## Copy and modify the above example so that the computer will 
## pick numbers between 1 and 4 instead.

# import random
# randomNumber = random.randint(1, 4)
# print(f"Here's a random integer: {randomNumber}")

######################################################################################################

## 1c
## Try this. Run it a few times.

# import random
# randomNumber = random.randint(5, 8)
# print(f"Here's a random integer: {randomNumber}")
# if randomNumber == 7:
#     print("I think some people say that number is lucky.")

######################################################################################################

## 1d
## Copy and modify the previous example so that the computer
## will pick numbers between 7 and 10 instead.

# import random
# randomNumber = random.randint(7, 10)
# print(f"Here's a random integer: {randomNumber}")
# if randomNumber == 7:
#     print("I think some people say that number is lucky.")

######################################################################################################

## 1e
## Copy and modify the previous example so that if the randomly
## chosen number is 10, it will say "Wow, a two digit number!"

# import random
# randomNumber = random.randint(7, 10)
# print(f"Here's a random integer: {randomNumber}")
# if randomNumber == 10:
#     print("I think some people say that number is lucky.")

######################################################################################################

## 2
## Try this.

# import random
# name = random.choice(["bob", "susan", "joe", "anna"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Your name rhymes with low.") 

######################################################################################################

## 3
## Copy and modify the above example so that "dell" is one of the names
## that can be randomly chosen.


# import random
# name = random.choice(["bob", "susan", "joe", "anna", "dell"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Your name rhymes with low.")

######################################################################################################

## 3b
## Copy and modify the above example so that 
## if the name is "dell", it will print "That’s a computer brand." 

# import random
# name = random.choice(["bob", "susan", "joe", "anna", "dell"])
# print(f"Hey {name}.") 
# if name == "joe":
#     print("Your name rhymes with low.")
# if name == "dell":
#     print("That's a computer brand")

######################################################################################################

## 4
## Try this.

# import random
# age = random.randint(18, 24)
# print(f"Pretend that you are {age} years old.")
# if age < 21: 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ") 

######################################################################################################

## 5
## Copy and modify the above example so that the legal drinking age is 40. (Just to be funny.)

# import random
# age = random.randint(18, 50)
# print(f"Pretend that you are {age} years old.")
# if age < 40: 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ") 

######################################################################################################

## 6
## Try this. Notice that it will ask for input. 

# thename = input("What is your name? \n")
# if thename == "george":
#     print("Are you named after the first US President?")
# else:
#     print("Hello.")

######################################################################################################

## 6b
## Change the previous example so that if the user types "bob", it will reply "Are you the painter?"

# thename = input("What is your name? \n")
# if thename == "george":
#     print("Are you named after the first US President?")
# elif thename == "bob":
#     print("Are you a painter?")
# else:
#     print("Hello.")

######################################################################################################

## 6c
## Try this.

# name = input("What is your name? \n") 
# if name == "joe": 
#     print("Your name rhymes with low.") 
# else: 
#     print(f"Hey {name}.") 

######################################################################################################

## 7b
## You'll notice that the user must type joe lowercase. Here's how to make it so any capitalization works:
# name.lower() reads the input as all lower case

# name = input("What is your name? ")
# if name.lower() == "joe": 
#     print("Your name rhymes with low.") 
# else: 
#     print(f"Hey {name}.") 

######################################################################################################

## 7c
## Try this. What do you think the != operator means?
# != means 'does not equal'

# name = input("What is your name? ")
# if name.lower() != "jay": 
#     print("Your name is not Jay.") 
# print("Greetings.")

######################################################################################################

## 7d
## Copy and modify the previous example like so:
## - Ask the user for a name
## - If the name is anything other than bob, then display "I don't think I know you. I only know Bob."

# name = input("What is your name? \n")
# if name.lower() != "bob": 
#     print("I don't think I know you. I only know Bob") 

######################################################################################################

## 7e
## Copy and modify the previous example like so:
## - Ask the user for a name
## - If the name is empty, say "You didn't type anything!"
## - Otherwise, say "Hi ___."
## Hint: an empty name would be quotes with nothing inside, so
##     you might use something similar to this piece of code:
##     if whatTheUserTyped == "":
##           print("Something would go here.")

# name = input("What is your name? \n")
# if name.lower() == "": 
#     print("You didn't type anything!")
# else:
#     print(f"Hi {name}!")


######################################################################################################

## 8 
## Try this. 

# age = 10 
# ageNextYear = age + 1 
# print(ageNextYear) 

######################################################################################################

## 9
## Try this. Note: you will get an error. 
# does not include int()

# age = input("How old are you?\n") 
# ageNextYear = age + 1 
# print(ageNextYear) 

######################################################################################################

## 10 
## Try this. 
# This fixes the above error

# age = int(input("How old are you?")) 
# ageNextYear = age + 1 
# print(ageNextYear) 

######################################################################################################

## 11
## Copy and modify the previous example to do the following: 
## - Ask the user for age 
## - Say "I see you are __ years old. You will be 65 years old in __ years."
##   For example, if the user typed 45, then it would display
##      "I see you are 45 years old. You will be 65 years old in 20 years."

# age = int(input("How old are you?\n")) 
# ageMath = 65 - age
# print(f"I see you are {age} years old. You will be 65 in {ageMath} years")

######################################################################################################

## 12
## Try this. Note: you will get an error.
# need to add int() for age
 
# age = input("How old are you?") 
# if age < 21: 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ") 

######################################################################################################

## 13
## Modify the above example so it works. You’ll use the `int` function. 

# age = int(input("How old are you?\n")) 
# if age < 21: 
#     print("You can't drink alcohol in the US yet.") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ") 

######################################################################################################

## 14
## Copy and modify the above example so that it shows how many years remain until you can
## drink (but only display that if you’re under the drinking age).

# age = int(input("How old are you?\n"))
# ageMath = 21 - age 
# if age < 21: 
#     print(f"You can legally drink in {ageMath} years") 
# else: 
#     print("You are legally allowed to drink. Drink responsibly 😊 ")

######################################################################################################

## 15
## Write a program that takes a name from the user. If the name is the letter "A", say
## "Your name is just the letter A? That’s kinda cool".  Otherwise, say "Ok, your name is ___".

# name = input("What is your name homie?\n")
# if name.lower() == "a":
#     print("Your name is just the letter A? That’s kinda cool")
# else:
#     print(f"Dopeeeeeee, your name is {name}")

######################################################################################################

## 16
## Try this: 

# birthyear = int(input("Type a year: ")) 
# if birthyear < 2000: 
#     print("You were born before 2000.") 
# elif birthyear == 2000: 
#     print("You were born in 2000.") 
# else: 
#     print("You were born after 2000.") 

######################################################################################################

## 16b
## Try this:

# name = input("What is your name? (type it lowercase please.)\n")
# print("Ok, let me look up that name...")
# if name == "bob":
#     print("That name used to be common, I think.")
# elif name == "sue":
#     print("Your name also refers to a legal action.")
# elif name == "rob":
#     print("Another abbreviation for robert, correct?")
# elif name == "lacy":
#     print("Does the origin of your name relate to clothing with lace?")
# else:
#     print("I don't know you.")
# print("Done.")

######################################################################################################

## 16c
## Try this. How is it different from the previous example?
## (The difference is subtle, so ask if you are unsure.)
# using only 'if' messes things up

# name = input("What is your name? (type it lowercase please.)")
# print("Ok, let me look up that name...")
# if name == "bob":
#     print("That name used to be common, I think.")
# if name == "sue":
#     print("Your name also refers to a legal action.")
# if name == "rob":
#     print("Another abbreviation for robert, correct?")
# if name == "lacy":
#     print("Does the origin of your name relate to clothing with lace?")
# else:
#     print("I don't know you.")
# print("Done.")

######################################################################################################

## 17
## Here's an example of using separate if statements,
## that is, a case where you would NOT want to use elif:

# name = input("What is your name? (type it lowercase please.)\n")
# print("Ok, let me look up that name...")
# if name.startswith("z"):
#     print("Your name starts with a Z. That is somewhat uncommon in English.")
# if len(name) < 3:
#     print("Your name is less than 3 characters long.")
# if len(name) > 9:
#     print("Your name is more than 9 characters long.")
# if name == "":
#     print("Your name is empty!")

######################################################################################################

## 17b
## Here's another example of the usefulness of elif.

# heightInInches = int(input("Give me a number: "))
# if heightInInches < 0:
#     print("You can't have a negative height!")
# elif heightInInches <= 55:
#     print("That's relatively short.")
# elif heightInInches <= 72:
#     print("That's around average.")
# else:
#     print("That's pretty tall.")

######################################################################################################

## 17c
## Copy and modify the previous example so that each `elif` is
## simply `if`. How does it act differently? 
# using just 'if' it reads the lines independently however
# using elif runs until the first instance occurs

# heightInInches = int(input("Give me a number: "))
# if heightInInches < 0:
#     print("You can't have a negative height!")
# if heightInInches <= 55:
#     print("That's relatively short.")
# if heightInInches <= 72:
#     print("That's around average.")
# else:
#     print("That's pretty tall.")

######################################################################################################

## 18
## Ask the user how many French fries they want.
## Display different responses depending on how many they
## request. (Examples: "That’s way too many!", etc.)

# fries = int(input("How many french fries would you like?\n"))
# if fries <= 9:
#     print(f"Come on fatty, I know you want more than {fries} fries.")
# elif fries <= 20:
#     print(f"There we go, {fries} fries is a good amount")
# else:
#     print(f"damn... {fries} fries is a lot.")

######################################################################################################

## 19
## Try this. Did it print what you expected?
# if x is less than 20, it prints a and b as well as c
# if x is greater than 20 it prints only c

# x = int(input("Enter a number: ")) 
# if x < 20: 
#     print("A") 
#     print("B") 
# print("C") 

######################################################################################################

## 20
## Copy and modify the previous example so that C is only printed if the number is not less than 20.
## Use the `else` keyword.

# x = int(input("Enter a number: ")) 
# if x <= 20: 
#     print("A") 
#     print("B")
# else: 
#     print("C") 

######################################################################################################

## 20b
## Copy and modify the previous example so that it acts like this:
## if x is less than 20, then print A.
## Otherwise, print C.
## After all of that is done, print Goodbye (regardless of what x was.)

# x = int(input("Enter a number: ")) 
# if x <= 20: 
#     print("A") 
# else: 
#     print("C") 
# print("Goodbye dawg")

############################################################################################################################################################################################################

## 21
## Ask the user for a number.
## If the user gives a number more than 50, 
##    then ask "What is your name?"
##    and display "Hello" followed by the name.
## If the user gives any other number,
##    then ask "How did you pick that number?"
##    and regardless of what they say, display "I see."
## After all of that, say "Have a good day."

# num = int(input("Give me a nummy... You know you wanna ;)\n"))
# if num >= 51:
#     name = input("What is your name homie?\n")
#     print(f"Hello {name}!")
# else:
#     how = input("How did you pick that number?\n")
#     print("Ya... I don't care, loser")
# print("have a good day!:)")

############################################################################################################################################################################################################


## 22
## Write a program that takes a number from the user.
## Display the number doubled.
## Then do a sequence of creative if statements of your choice.
##   For example, if the number is negative, display "Really? Negative? Interesting".

# num = int(input("Give me nummy!\n"))
# print(f"That nummy doubled is {num * 2}")
# if num < 0:
#     print("You like negative numbers? loser")
# else:
#     print("YAYYYY positive numbers rock!")

############################################################################################################################################################################################################

## 22b
## Try this. Why do we use float instead of int here?
#since we are doing division that commonly results in floating point nummies

# firstcost = float(input("How much is the first thing you bought? "))
# secondcost = float(input("How much is the second thing you bought? "))
# total = firstcost + secondcost
# discounted = total * 0.9
# print(f"The total cost would be {total}.")
# print("However, we're doing a special sale today, so you get a 10% discount.")
# print(f"That means you actually pay {discounted}")

############################################################################################################################################################################################################

## 23
## Try this.
# x = float(input("Type a number between 0 and 1, for example, 0.3, 0.25, etc... "))
# print(f"One more would be {x + 1}.")

## As you can see, you can use `float` instead of `int` when dealing with non-whole numbers.
## Sidenote: 
##   (this sidenote is outside the scope of the class, but good to know)
##   Using floats can cause weird rounding errors. For example:
# print(1.03 - 0.42)

##   This will print 0.6100000000000001.
##   That's quite important when doing comparisons:
# if 0.1 + 0.1 + 0.1 == 0.3:
#     print("This will not print.")
# else:
#     print("This will print... what is math??")

##   The reason is because the numbers are converted to binary behind the scenes,
##   and just as you can't express "one third" exactly in decimal (0.33333 is not EXACTLY one third)
##   you can't express "one tenth" exactly in binary.
##   For more info, see https://docs.python.org/3/tutorial/floatingpoint.html
##   If you plan to eventually do any "real-life" programming, then it's definitely worth reading.
## (end of sidenote)

############################################################################################################################################################################################################

## 23b
## Ask the user for the cost of a single item and the quantity purchased. Print the total cost. 
## Make sure this works for non-integer costs. For example, try a cost of 2.30 and quantity of 2.
## Hint: You'll use float instead of int.
## Example:
## What is the cost for an item? 2.30
## How many did you buy? 2
## The total cost would be $4.60.

# item1 = float(input('How much was your first item?\n'))
# quant1 = float(input('How many of those items did you buy?\n'))
# print(f'Your total cost is ${item1 * quant1}')

############################################################################################################################################################################################################

## 24
## Modify the previous example so that the shop gives a discount of 10% if you buy at least 20 of an item.  
## For example, if one item costs $5, and you’re buying 20, total cost would be $90. 

# item1 = float(input('How much was your first item?\n'))
# quant1 = float(input('How many of those items did you buy?\n'))
# cost = item1 * quant1
# discount = cost * 0.1
# if quant1 <=19:
#     print(f'Your total cost is ${cost}')
# else:
#     print(f'Your final cost is {cost - discount}')

############################################################################################################################################################################################################

## 25
## Ask the user for a number (make sure to allow for non-whole numbers).
## Print the absolute value of the number without using the abs function. 

# num = float(input('give me nummy!\n'))
# if num < 0:
#     print(f'The adsolute value of {num} is {num * -1}')
# else: 
#     print(f'The absolute value of {num} is {num}')

############################################################################################################################################################################################################


## 26
## Ask the user for a temperature in Celsius, and display the temperature in Fahrenheit. 
## Make sure to allow for non-whole numbers.

# temp = float(input('Give me a temp is Celsius: \n'))
# tempF = (temp * 9/5) + 32
# print(f'{temp} degrees Celsius equals {tempF} degrees Fahrenheit')

############################################################################################################################################################################################################

## 27
## Same as previous example, but backwards. 

# temp = float(input('Give me a temp is Fahrenheit: \n'))
# tempC= (temp -32) * 5/9
# print(f'{temp} degrees Fahrenheit equals {tempC} degrees Celsius')

####################################################################

## 28
## Combine the two previous examples: ask the user for a number and which way to convert. 

# temp = float(input('Give me a tempature \n'))
# tempType = input('Is that degrees F or C (Enter F for Fahrenheit and C for Celsius):\n')
# if tempType.lower() == 'c':
#     tempF = (temp * 9/5) + 32
#     print(f'{temp} degrees Celsius equals {tempF} degrees Fahrenheit')
# if tempType.lower() == 'f':
#     tempC = (temp -32) * 5/9
#     print(f'{temp} degrees Fahrenheit equals {tempC} degrees Celsius')

########################################################################################################################################

## 29
## Ask the user for a number.
## Using the % operator, display "The remainder of your number divided by 5 is ___."
## Also, if the remainder that you calculated is 0, display "That number is evenly divisible by 5."

# num = int(input('Give me a nummy: \n'))
# numMath = num % 5
# if numMath == 0:
#     print(f'{num} is evenly divisable by 5')
# else:
#     print(f'The remainder of {num} divided by 5 is {numMath}')

############################################################################################################################################################################################################

## 30
## Try this.

# color = input("What color is water? ")
# if color == "blue" or color == "transparent":
#     print("Yes, I agree.")
# else:
#     print("I'm not sure about that.")

############################################################################################################################################################################################################

## 31
## Try this.

# color = input("What color is water? ")
# if color in ["blue", "transparent"]:
#     print("Yes, I agree.")
# else:
#     print("I'm not sure about that.")

############################################################################################################################################################################################################

## 32
## Try this.

# color = input("What color is water? ")
# if color != "blue" and color != "transparent":
#     print("I'm not sure about that.")
# else:
#     print("Yes, I agree.")

############################################################################################################################################################################################################

## 33
## Try this.

# color = input("What color is water? ")
# if color not in ["blue", "transparent"]:
#     print("I'm not sure about that.")
# else:
#     print("Yes, I agree.")

############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################