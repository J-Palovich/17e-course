############################################################################################################################################################################################################

### Lists are zero-indexed. That means...
thelist = ["water", "chair", "mug", "mouse", "dog", "cat", "dolphin", "emu", "monkey"]
             # 0      1        2      3 

### Example:

# print(thelist[0])    # This will print water
# print(thelist[2])    # What will this print?

###########################################################################################################################################################

# 1
# Try this. Do you expect it to print “water” or “chair”?
# Prints CHAIR

# thelist = ["water", "chair", "mug", "mouse"]
# print(thelist[1])

############################################################################################################################################################################################################

# 2
# Modify the previous example to print the fourth element of the list (“mouse”).

# thelist = ["water", "chair", "mug", "mouse"]
# print(thelist[3])

############################################################################################################################################################################################################

# 3
# Try this. Do you expect an error?
# Reads the list backwards starts are 1

# print(thelist[-1])
# print(len(thelist)) Prints how long the list is

############################################################################################################################################################################################################


# 4
# Add a few elements to thelist. Then do this again:
# print(thelist[-1])

############################################################################################################################################################################################################

# 5
# Now make it print the second-to-last element of thelist.
# print(thelist[-2])

############################################################################################################################################################################################################

# 6
# Try this. Which items does it display? 
# Does it include all of the items you expected? 
# (It’s a little counterintuitive.)
# this prints the first, second and third item in the list

# print(thelist[0:3])

############################################################################################################################################################################################################

# 7
# Try this.
# this prints the second and third item in the list
# print(thelist[1:3])

############################################################################################################################################################################################################

# 8
# Modify the previous example to print elements 0,1,2,3. (Hint: it’s not going to be [0:3], but it’s close to that.)
# print(thelist[0:4])

############################################################################################################################################################################################################

# 9
# Try this.
# since to end it specified, it prints the entire list starting at the second item
# print(thelist[1:])

############################################################################################################################################################################################################

# 10
# Modify the previous example to print all but the first two items.
# Pretend you don’t know how long the list is. (You shouldn’t need to.)
# print(thelist[2:])

############################################################################################################################################################################################################

# 11
# You can change an item in the list using the following approach.
# How could you verify that the list was changed?
# specify the list and the position and the new value and print the list

letters = ["a", "b", "c", "d", "e"]
# letters[0] = "ROCKET"
# print(letters)

############################################################################################################################################################################################################

# 12
# Modify the previous example to replace "d" with "WAVE".
# letters[3] = "wave"
# print(letters)

############################################################################################################################################################################################################

# 13
# Modify the previous example to use negative indexing
# letters[-2] = 'wave'
# print(letters)

############################################################################################################################################################################################################

# 14
# Try this.
# name = "Becky"
# print(name[0])


############################################################################################################################################################################################################

# 15
# Modify the previous example to print the “c” of “Becky”.
# name = "Becky"
# print(name[2])

############################################################################################################################################################################################################

# 16
# Try this.
# selects the item in the list then the character in the item
names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names[4][3])

############################################################################################################################################################################################################

# 17
# Modify the previous example to print the last letter of Sarah’s name (using string indexing).
# print(names[0][-1])

############################################################################################################################################################################################################


# Modify the previous example to print the last letter of the last name in the list. Use negative indexing.
# print(names[-1][-1])

############################################################################################################################################################################################################

# 19
# Try this.
# concatenates the second item in the named list (not using print(f''))
# makes variable the string

# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# sentence = "Hello to " + names[1] + " and everyone else."
# print(sentence)

############################################################################################################################################################################################################

# 20
# Try this.
# concatenates the second item in the named list ( using print(f''))

# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(f"Hello to {names[1]} and everyone else.")

############################################################################################################################################################################################################

# 21
# Try this.

# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# id_num = 4
# print(f"ID: {id_num} Name: {names[id_num]}")

############################################################################################################################################################################################################

# 22
# Copy and modify the previous example to
# ask the user for a student id, and then
# displays "The student with id number ___ is named ___".

# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# id_num = int(input('Please enter student ID:\n'))
# try:
#     print(f"The student with ID number {id_num} is named {names[id_num]}")
# except Exception:
#     print('Please enter valid student ID')

############################################################################################################################################################################################################

# 23
# You can add an item to the end of a list using append:

# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names)
# names.append("Bob")
# print(names)

############################################################################################################################################################################################################

# 24
# Copy and modify the previous example so that it asks the user
# for a new name that you want to add to the end of the list.

# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names)
# names.append(input('Enter a name you would like to add to the list above:\n')) 
# print(names)

############################################################################################################################################################################################################

# 25
# You can remove items using del:

# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names)
# del names[0]
# print(names)

############################################################################################################################################################################################################

# 26
# Copy and modify the previous example so that it asks the user
# for a position (that is, the index) in the list. Remove that item
# from the list using del, and then display the changed list.

# names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
# print(names)
# del names[int(input('Select an index to delete from above (Start at 0):\n'))]
# print(names)

############################################################################################################################################################################################################

# 27 
# A list can be generated using the range() function.
# Try this:
# start = 1
# stop = 10+1
# step = 2
# num_list = list(range(start, stop, step))  
#   # range parameters: start #, stop#+1, increment (i.e., the "count by" value)
#   # Note: Range always omits the final number, so a "+1" has been added 
#   # to shown what the actual stopping number will be.  In this example the stop will occur at 10.
# print(num_list)

############################################################################################################################################################################################################

# 28
# Modify the previous example to create a list that includes all numbers  
# between 0 and 30 that are divisible by 3.  
# Note: 0, 1, 2, 4, etc. are not divisible by 3.  Do not include them.

# start = 0
# stop = 30 + 1
# step = 3
# numList = list(range(start, stop, step))
# print(numList)



############################################################################################################################################################################################################

# names = []
# print(names)
# ans = input('Would you like to add or remove names from the list above (say "a" or "r"):\n')
# if ans.lower() == 'a':
#     names.append(input('What name would you like to add: \n'))
#     print(names)
# if ans.lower() == 'r':
#     try:
#         del names[int('Select the index to delete (Starting at 0):\n')]
#     except Exception:
#         print('Please enter a valid index')


############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################

