
# Importing the random library
import random

# Asking the user for a name
print('Hi, What is your name?')
name=input()

# Setting a variable with a random number
secretNumber=random.randint(1,20)

print('Okay '+name+'. We will play a game. You have to guess a number between 1 and 20. You have 5 guesses.')

# Starting the loop with the guesses
for guessesTaken in range (1,6):
    try:
        print('Take a guess.')

        # Asking the user for a guess
        guess=int(input())

        if guess>20 and guess<1:
            print('Please '+name+', type a number between 1 and 20')
        elif guess<secretNumber:
            print('Too low.')
        elif guess>secretNumber:
            print('Too high.')
        else:
            print('That is correct. Well done')
            break

    except ValueError:
        print('Please '+name+', type a number between 1 and 20')

if guess==secretNumber:
    print(name+', you did it in '+str(guessesTaken)+' guesses.')
else:    
    # Printing a message if the user did not guess the number
    print('I am sorry '+name+'. You did not guess it.')
