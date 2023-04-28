## EXERCISES ------------------------------------------------------------------------
## Valid variable names -- These are examples of valid variable assignment statements:
mynumber = 7
temp_in_f = 8.3
my2ndthing = "hi"
x3 = "stuff"
_myStuff = 7
result = mynumber * _myStuff

# This definition of a variable is valid, but please don't, because "input" will no longer be a function.
# input = 7

## Using variables: 
## These statements reference/use the variables defined in the "Valid variable names" section, above.
print(mynumber)
print(f"The recorded temperature is {temp_in_f}°F")
print(f"The following message was received '{my2ndthing}'.")
print(f"The result of multiplying", mynumber, "and", _myStuff, "is equal to", result)

#############
# invalid:
#############

# Can't use keywords, as an example: 
# if = 6
# (After trying the previous line, delete it, or convert it to a comment by proceeding it with a number/pound symbol (#).)

# Can't start with number
# 3rdthing = "hi"

# Can't have spaces inside of the name
# my var = 3

# Can't have special characters (only "_" is allowed inside a variable name)
# $d = 6