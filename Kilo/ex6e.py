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

# ----------------------------------------------------------------------------------------------------------------------#
import random
gameChoice = ''
print('Welcome to the games terminal!')

while gameChoice != 'q':

    gameChoice = input("Would you like to play 'Word Guess' or 'Number Guesser'? (Enter w or n): ")
    print()
    # ----------------------------------------------------------------------------------------------------------------------#
    # WORD GUESSING GAME
    if gameChoice.lower() == 'w':

        playAgain = 'yes'
        print()
        wordGuess = ''
        magicWords = ['banana', 'hope', 'stars',
                    'whiskey', 'fight', 'money']
        word = random.choice(magicWords)
        hints = [f'The word starts with a {word[0]}',
                f'The word ends with a {word[-1]}',
                f'The word has a {word[3]} in it']
        count = 1
    # ----------------------------------------------------------------------------------------------------------------------#
        while playAgain.lower() == 'yes':

            print('Welcome to the word guessing game!\n')
            wordGuess = input('Take your first guess at my word: ')
    # ----------------------------------------------------------------------------------------------------------------------#
            while wordGuess.lower() != word:
                if wordGuess.lower() != word:
                    count += 1
                if count == 3 or count == 6 or count == 9:
                    hint = input('Would you like a hint? (yes / no):\n')
                    if hint.lower() == 'yes':
                        print(random.choice(hints))
                wordGuess = input(f'Guess {count}: ')
    # ----------------------------------------------------------------------------------------------------------------------#
                if wordGuess.lower() == word:
                    print(f"Congratulations! You guessed the word in '{word}' in {count} guesses.\n")
                    playAgain = input(f'Would you like to play again? \n')
                    count = 1
                    if playAgain.lower() != 'yes':
                        print('Thank you for playing!')
    # ----------------------------------------------------------------------------------------------------------------------#
    elif gameChoice.lower() == 'n':

        playAgain = 'yes'
        print()
        numGuess = ''
        num = random.uniform(0, 1000)
        count = 1
        # print(int(num))
 # ----------------------------------------------------------------------------------------------------------------------#
# NUMBER GUESSING GAME
        while playAgain.lower() == 'yes':
            print('Welcome to the number guessing game!\n')
            numGuess = int(input('Take your first guess at my number: '))
 # ----------------------------------------------------------------------------------------------------------------------#

            while numGuess != int(num):
                if numGuess != int(num):
                    count += 1
                    if numGuess > int(num):
                        print(f'{numGuess} is too high.')
                        numGuess = int(input(f'Guess {count}: '))
                    if numGuess < int(num):
                        print(f'{numGuess} is too low.')
                        numGuess = int(input(f'Guess {count}: '))
 # ----------------------------------------------------------------------------------------------------------------------#

                if numGuess == int(num):
                    print(f"Congratulations! You guessed the number in '{int(num)}' in {count} guesses.\n")
                    playAgain = input(f'Would you like to play again? \n')
                    count = 1
                    if playAgain.lower() != 'yes':
                        print('Thank you for playing!')
        
# ----------------------------------------------------------------------------------------------------------------------#

    elif gameChoice == 'q':
        print('Thank you for playing!')
# ----------------------------------------------------------------------------------------------------------------------#

    else:
        print("Please enter 'w' for Word Guess, 'n' for Number Guesser or 'q' to quit: ")
