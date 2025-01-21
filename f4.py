print('How many dogs do you have?')

# Asking the user for a number
numDogs=input()

# Throwing the try-except statement
try:
    if int(numDogs) >= 4:
        print('That is the right answer. We love dogs.')
    elif int(numDogs) < 0:
        print('You can not submit a value smaller than cero.')
    else:
        print('You need more dogs.')

# Catching the exception. If the user types in a value different than a number, we print a message.
except ValueError:
    print('You did not enter a number')