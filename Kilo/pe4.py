# Prompt the user: "Ask the 8 ball a question, or enter 'no' to quit"

# -- If the user asks any question, then randomly display one of these replies: 
#    It is Certain
#    Yes
#    You may rely on it
#    Ask again later
#    You've Got to be Kidding
#    Reply hazy, try again
#    My reply is NO WAY
#    My sources say no

# -- If the user enters "no", then say "Goodbye. See you next time."
#    The user must be able to type "no", "No", "nO", or "NO".

# Note: For this PE, a loop is NOT required.

# ----------------------

# Rubric:
# 10%  Prompts the user to ask a question
# 25%  If the user enters anything other than 'no', displays a random reply.
# 15%  If the user enters anything other than 'no', does NOT display the "Goodbye" message.
#        (E.g., Does not display "Goodbye..." if user asks a question.)
# 25%  If the user enters 'no', displays the "Goodbye" message
# 15%  If the user enters 'no', does NOT display a random reply
# 10%  In all above cases where "no" is mentioned, the logic works correctly for any capitalization

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
    if question.lower() == 'no':
        break 
    response = random.choice(ans)
    print(response)
    print()
    

print('Goodbye, see you next time.')






