import re

message="Call me at 012-345-6789"

# Telling the RE that we want 3 digits followed by a dash, another 3 digits followed by a dash, and 4 digits at the end
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Searching the message for any matches
phone=phoneNumRegex.search(message)

# Printing the match
print(phone.group())

message="Call me at 012-345-6789"

# Telling the RE that we want 3 digits inside a parens, then followed by a dash, another 3 digits followed by a dash, and 4 digits at the end all within a parens
phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# Searching the message for any matches
phone=phoneNumRegex.search(message)

# Printing the match for the first group (3 first digits)
print(phone.group(1))

# Printing the match for the second group (7 remaining digits)
print(phone.group(2))

# Using the pipe '|' in the regex string lets you match one of many groups
batRegex=re.compile(r'Bat(cave|man|mobile)')
batMessage=batRegex.search('Batman v. Superman: Dawn of Justice')
print(batMessage.group())

batMessage=batRegex.search('Batmobile lost a wheel')

# By adding 1 to the group, it will print the match text of the group
print(batMessage.group(1))

# Adding the question mark at the end of a parent makes that part optional
batRegex=re.compile(r'Bat(wo)?man')
batMessage=batRegex.search('The adventures of Batwoman')
print(batMessage.group())

# ? 0 or once
# * 0 or multiple times
# + once or multiple times

message="Call me at 012-345-6789,923-981-9293,010-657-8231"

# By adding a number between curly braces, it will match that number of times
phoneNumRegex=re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
phone=phoneNumRegex.search(message)
print(phone.group())

# By adding another parens in the regex string, it will print any match in groups. 
phoneNumRegex=re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')

# The findall method prints the whole match
print(phoneNumRegex.findall(message))

lyrics="12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree"

# \d is used for digits
# \s is used for whitespaces
# \w is used for word characters
xmasRegex=re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# Adding a '^' means that the string must start with that pattern
beginsWithHelloRegex=re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello'))

# Adding a '$' means that the string must end with that pattern
endsWithHelloRegex=re.compile(r'world!$')
print(endsWithHelloRegex.search('Hello world!'))

# Telling the code that the pattern must start and end with digits
allDigitsRegex=re.compile(r'^\d+$')
print(allDigitsRegex.search('82829349478932348'))
print(allDigitsRegex.search('8282934947893xxx2348'))

# Searching for all the words that has 3 letters and ends in at
atRegex=re.compile(r' .at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# Searching for all the words that has 3 or 4 letters and ends in at
atRegex=re.compile(r' .{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex=re.compile(r'First Name: (.*) Last Name: (.+)')
print(nameRegex.findall('First Name: Jorge Last Name: de la Serna'))

serve='<To serve humans> for dinner.>'

# Nongreedy will try to match the shortest string possible
nongreedy=re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

# Greedy will try to match the longest string possible
greedy=re.compile(r'<(.*)>')
print(greedy.findall(serve))

prime='Serve the public trust.\nProtect the innocent.\nUpload the law.'

# Adding a '.' will match anything except newlines
dotStar=re.compile(r'.*')
print(dotStar.search(prime))

# By adding 're.DOTALL', it will tell the code to match newlines too
dotStar=re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))

# Searching for all the lower case vowels
vowelRegex=re.compile(r'[aeiou]')
print(vowelRegex.findall('Al, why does your programming book talk about Robocop so much?'))

# Passing 're.I' makes it case-insensitive
# Searching for all the vowels
vowelRegex=re.compile(r'[aeiou]',re.I)
print(vowelRegex.findall('Al, why does your programming book talk about Robocop so much?'))

# Searching for as many matches match the pattern given
namesRegex=re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))

# The sub method will replace some text with other text
print(namesRegex.sub('Agent', 'Agent Alice gave the secret documents to Agent Bob'))

namesRegex=re.compile(r'Agent (\w)\w*')

# Using \1, \2, and so will substitute group 1,2 etc in the regex pattern
print(namesRegex.sub(r'Agent \1**', 'Agent Alice gave the secret documents to Agent Bob'))

# Passing re.VERBOSE lets you format the regex string and add comments to it
re.compile(r'''
    (\d\d\d-)|      # aera code without parens and with dash
    (\(\d\d\d\) )   # -or- area code with parens and no dash
    \d\d\d          # first 3 digits
    -               # second dash
    \d\d\d\d        # last 4 digits
    \sx\d{2,4}      # extension, like x1234
           ''',re.VERBOSE)