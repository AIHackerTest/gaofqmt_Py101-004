from random import randint
from sys import exit

#Make sure the user enters a number

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an interger! Try again.")
            continue
        else:
            return userInput
            break

guesses = 0
code = randint(1, 20)

while True: 
    if guesses:
        print("You still have %d times!" % (10 - guesses))
    guess = inputNumber("Please enter a number between 1 and 20:") 

    guesses += 1
    if guesses == 10:
        print("You failed the game!")
        exit(1)
    elif guess == code:
        print("Congratulations, You win!")
        break
    elif guess > code:
        print("Your number is bigger!")
        continue
    else:
        print("Your number is smaller!")
        continue



