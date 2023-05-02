
import random

beats = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
    }

choices = ["rock", "paper", "scissors"]
user = ''
cpu = ''
userCount = 0
cpuCount = 0
again = True


while again == True:

    if userCount != 0 or cpuCount != 0:
        print(f'Score:\nYou: {userCount}\ncpu: {cpuCount}\n')

    try:
        user = input("rock paper or scissors? ")
        cpu = random.choice(choices)
        print(f"cpu has selected: {cpu}\n")

        if user == cpu:
            print("Tie")
            again 
        if beats[user] == cpu:
            userCount += 1
            if userCount != 3:
                again
            else:
                print("You win!")
                
        if beats[cpu] == user:
            cpuCount += 1
            if cpuCount != 3:
                again
            else:
                print("You lose!")
                again = False

    except Exception:
        print('Please enter Rock, Paper, or Scissors')