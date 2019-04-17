#this is a guess number game
import random

def guessTheNumber(secretNumber):
    #ask the player to guess 6 time
    for guessesTaken in range(1,7):
        print('Take a guess: ')
        guess=int(input())

        if guess>secretNumber:
            print('Your guess is too high')
        elif guess<secretNumber:
            print('Your guess is too low')
        else:
            break
    if guess==secretNumber:
        print('Good job!you gussed my number is '+str(guessesTaken)+' guesses!')

    else:
        print('Nope.The number I was thinking of was '+str(secretNumber))

secretNumber=random.randint(1,20)
print('I am a thinking of a number between 1 and 20.')
guessTheNumber(secretNumber)
