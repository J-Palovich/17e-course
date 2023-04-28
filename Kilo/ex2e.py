
#########################################################################################################

## 1
## Ask the user for two numbers.
## Display "If you divided ___ by ___, then you would get ____ with a remainder of ___".
## You'll want the modulus operator. Look up how to do remainder (or modulus) in Python.
## You may also want the floor division operator.

# num1 = float(input("gimme nummy 1:\n"))
# num2 = float(input("gimme nummy 2: \n"))
# print(f"If you divide {num1} by {num2}, then you would get {num1 / num2} with a remainder of {num1 % num2}")

#########################################################################################################

## 2: Calculating an exponent
## Ask the user for two numbers.
## Display "If you computed ___ to the power of ___, then you would get ___."
## (Hint: What is the operator for exponent in Python? It may not be what you think.)

# num3 = float(input("gimme nummy 3:\n"))
# num4 = float(input("gimme nummy 4: \n"))
# print(f"if you computed {num3} to the power of {num4}, then you would get {num3 ** num4}")

#########################################################################################################

## 3: Operators that may not do what you expect
## Based on question #1, does % calculate a percentage? (Answer: No)
# % gets remainder
## Based on question #2, does ^ calculate an exponent? (Answer: No)
# ** does exponents and ^ does jack shit

#########################################################################################################

## 4
## Try this. As you can see, it's possible to reassign variables.

# x = 3
# print("Currently, x is...")
# print(x)
# x = 4
# print("Now, x is...")
# print(x)

#########################################################################################################

## 5
## Try this. It's a little counter-intuitive.

# x = 3
# print("Currently, x is...")
# print(x)
## You should read the line below as "Set x to 5 more than what x used to be."
# x = x + 5
# print("Now, x is...")
# print(x)

#########################################################################################################

## 6
## Python provides another equivalent way to do this:

# x = 3
# print("Currently, x is...")
# print(x)
# x += 5
# print("Now, x is...")
# print(x)

#########################################################################################################
