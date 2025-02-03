message="Hello World!"

print(message)

# Printing the message to lowercase
print(message.lower())

# Printing the message to uppercase
print(message.upper())

# Checking if the message is all uppercase
print(message.isupper())

# Checking if the message is all lowercase
print(message.islower())

# Checking if the message is all letters
print(message.isalpha())

# Checking if the message is all letters and numbers
print(message.isalnum())

# Checking if the message is all numbers
print(message.isdecimal())

# Checking if the message is all white spaces
print(message.isspace())

# Checking if every word in the message is capitalize
print(message.istitle())

# Checking if the message starts with 'H'
print(message.startswith("H"))

# Checking if the message starts with 'o'
print(message.startswith("o"))

# Checking if the message ends with '!'
print(message.endswith("!"))

# Checking if the message ends with 'o'
print(message.endswith("o"))

# Adding white spaces(default) at the start of the message until hitting 20 characters
print(message.rjust(20))

# Adding dashes at the end of the message until hitting 20 characters
print(message.ljust(20,"-"))

# Adding dashes at the start and end of the message until hitting 20 characters
print(message.center(20,"-"))

# Removing a string from the message
print(message.strip("Hello"))

# Removing all white spaces after the text from the message
print("           Hello World!           ".rstrip())

# Removing all white spaces before the text from the message
print("           Hello World!           ".lstrip())

# Replacing a string from the message
print(message.replace("World", "Python"))
