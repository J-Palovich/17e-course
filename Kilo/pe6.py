# This will be similar to your "8 ball" PE.
# In this new version, instead of only asking once, use a loop:
# - If the user enters "no" or "n", then display the "Goodbye" text (as 
#     you did before), and stop asking questions.
# - If the user says anything else, then display a 
#     randomly selected answer (as you did before), and
#     continue asking.

# As before, it must act the same if the user types "no", "No", "nO", or "NO".

# ----------------------

# Rubric:
#  5%  Prompts the user to ask a question
# 10%  If the user enters anything other than 'no', displays a random reply 
# 10%  Random reply is randomized in each iteration (no credit if 
#      it only picks the random reply once at the beginning of the program)
# 20%  Continues to prompt the user for questions until the user says 'no'
# 15%  If the user enters 'no' or "n", displays the "Thanks" message   
# 10%  If the user enters 'no' or "n", does NOT display a random reply
# 20%  If the user enters 'no'  or "n", stops asking questions
# 10%  In all above cases where "'no' or 'n'" is mentioned, the logic works correctly for any capitalization

import random

question = ''
ans = ['It is certain',
       'Yes',
       'You may reply on it',
       'Ask again later',
       'You got to be kidding',
       'Reply hazy, try again',
       'My reply is NO WAY',
       'My sources say no']

while question.lower() != 'no':
    question = input("Ask the 8 ball a question, or enter 'no' to quit: \n")
    if question.lower() == 'no'or question.lower() == 'n':
        break 
    response = random.choice(ans)
    print(response)
    print()
    

print('Goodbye, see you next time.')
