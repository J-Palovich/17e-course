########################################################################################################################################################################################################################################################################################################################################################################################################################

# 1
# Try this. 
# It won't display anything to the screen -- rather, it creates a file.
# Try to find the file it created.


# f = open("ex7a.txt", "w")
# f.write("Here are some words.\n")
# f.write("More words.")
# f.close()

########################################################################################################################################################################################################################################################################################################################################################################################################################

# 2
# Using Python,
# Open the file my_thoughts.txt.
# Write at least 10 separate lines in it.
# Close the file.

# f = open("thought.txt", "w")
# f.write("line 1\nline 2\nline 3\nline 4\nline 5\nline 6\nline 7\nline 8\nline 9\nline 10\n")
# f.close()

########################################################################################################################################################################################################################################################################################################################################################################################################################

# 3
# Using Python,
# Ask the user for name and age.
# Open a file called person_info.txt.
# Write in that file, "___ is ___ years old" (with the name and age filled in).
# Close the file.

# name = input('Hello user! What is your name?\n')
# age = int(input('Thank you, What is your age?\n'))

# f = open("txtfiles/userInput.txt", "w")
# f.write(f"{name} is {age} years old.")
# f.close()


########################################################################################################################################################################################################################################################################################################################################################################################################################

# 4
# Try this.

# f = open("txtfiles/userInput.txt", "r")
# contents = f.read()
# print(contents)
# f.close()

########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################