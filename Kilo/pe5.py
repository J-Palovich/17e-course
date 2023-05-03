# Ask the user for a student's name.
# Ask for his/her grade in math, science, and history.
# Print "_____'s average is _____"
# (Fill in the actual name and average.)

# Also, create a data file (using Python) called "calculated_average.txt".
# In that file, write the same text:
# "_____'s average is _____"
# Close the file using the .close() method, as shown in examples.

# Note 1: For all number inputs, non-whole-number entries should be allowed.
# Note 2: In the "output" field (below) paste the following
#    (1) command line data (as in earlier PEs), even if minimal,
#    (2) This separator line: " ------ Data file follows. ---------", and
#    (3) The contents of the data file your program created.

# ----------------------

# Rubric:
# 10%  Asks for name and grades (asks for all three grades)
# 10%  Inputs allow for non-whole numbers
# 30%  Displays "_____'s average is _____" with the 
#        user-provided name and the average of
#        the user-provided grades
# 20%  Average is calculated correctly
# 10%  Creates a file called "calculated_average.txt"
# 20%  Writes the aforementioned text to the file

studentName = input('Please enter student name: ')
mathGrade = float(input('Input student grade in Math: '))
scienceGrade = float(input('Input student grade in Science: '))
historyGrade = float(input('Input student grade in History: '))
averageGrade = (mathGrade + scienceGrade + historyGrade) / 3

ave = f"{studentName}'s average is {averageGrade}"
print(ave)

f = open("calculated_average.txt", "w")
f.write(ave)
f.close()