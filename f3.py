# How to import a Python library
import random, sys, os, math
1
# Setting the variable 'num' with a random number between 1 and 10
num=random.randint(1,10)

# Printing a message with the random number
print('Your random number is ...', num)

# With this code, the program will end and not execute the code after it.
# sys.exit()
# print('Goodbye')

# Creating our own function
def checking_age(age):
    # 'result' is a local scope and can only be access within the function
    if age<19:
        result='You are underage.'
    elif age>19 and age<65 :
        result='You are an adult.'
    else:
        result='You are senior citizen'
    return result
print('Hi, how old are you?')
age=input()

# Calling the function and converting the input from the user to be an int
print(checking_age(int(age)))