# This creates a list where each position of the list is a word 
text=['Hello', 'this', 'is', 'a', 'list']

# This prints the value of the position 0 in the list text
print(text[0])

# This prints the value of the last position in the list text
print(text[-1])

# Creating the list supplies with 4 values in it
supplies=['pens', 'staplers', 'flame-throwers', 'binders']

# Creating the loop with the number of values in the list supplies
for i in range(len(supplies)):
    # For each index of the list, we print its value
    print('Index '+str(i)+' in supplies list is: '+supplies[i])

# Creating two variables
a='AAA'
b='BBB'

# Printing the two variables with a message
print('Variable a has '+a+' while variable b has '+b)

# By doing the next line of code, we swap the value of the variable 'A' to variable 'B' and viceversa
a, b = b, a
print('Variable a has '+a+' while variable b has '+b)

# Adding index, returns the position of the value in the list
print(supplies.index('staplers'))

# Adding append, adds a new value to the end of the list
supplies.append('pencil')
print(supplies)

# Adding insert, adds a new value anywhere inside the list
supplies.insert(2, 'paper')
print(supplies)

# Adding remove, removes the specified value from the list
supplies.remove('flame-throwers')
print(supplies)

# Creating a new list with numbers
numbers=[20,40,90,50,30,10]
print(numbers)

# Adding sort to the list, sorts the list from lower to higher
numbers.sort()
print(numbers)

# Adding reverse=true to sort, sorts the list in reverse order
numbers.sort(reverse=True)
print(numbers)