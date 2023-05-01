# Make a word guessing game. The user should be able
# to continue guessing until guessing the word correctly 
# (regardless of uppercase/lowercase). Every time the user
# guesses, you should display how many guesses the user 
# has taken so far. Give special messages after certain
# guesses -- for example, after the third guess, say 
# "Three strikes, you're out! Just kidding, you can keep
# guessing." Note: For extra fun, use the Python termcolor module.

# Make a number guessing game. Give the user feedback with
# each guess: "Too high" or "Too low".

import random
playAgain = 'yes'
print()
guess = ''
magicWords = ['banana', 'hope', 'stars',
             'whiskey', 'fight', 'money']
word = random.choice(magicWords)
hints = [f'The word starts with a {word[0]}',
         f'The word ends with a {word[-1]}'
         f'The word has a {word[3]} in it']
count = 1

while playAgain.lower() == 'yes':

    print('Welcome to the word guessing game!\n')
    guess = input('Take your first guess at my word: ')

    while guess.lower() != word:
        if guess.lower() != word:
            count += 1
        if count == 3 or count == 6 or count == 9:
            hint = input('Would you like a hint? (yes / no):\n')
            if hint.lower() == 'yes':
                print(random.choice(hints))
        guess = input(f'Guess {count}: ')

        if guess.lower() == word:
            print(f"Congratulations! You guessed the word in '{word}' in {count} guesses.\n")
            playAgain = input(f'Would you like to play again? \n')
            count = 1
            if playAgain.lower() != 'yes':
                print('Thank you for playing!')
            



        
    

