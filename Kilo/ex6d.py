########################################################################################################################################################################################################################################################################################################################################################################################################################

# Using .split() outputs each word seperated by a space on a new line 
# .splitlines() outputs each line on a new line

f = open("Kilo/names.txt", "r")
lines = f.read().splitlines()
for line in lines:
    print(f"{line}'s username is {line[0]}")

########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################
######################################################################################################################################################################################################################################################################################################################################