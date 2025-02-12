import webbrowser, sys

# Storing command-line arguments
sys.argv # ['f12.py', '1820', ' Market St']

address=''

# Checking if there is more than 1 argument
if len(sys.argv) > 1:
    # Merging all the arguments but the first
    address=' '.join(sys.argv[1:])
else:
    print('The program expects more than 1 argument.')

link='https://www.google.com/maps/place/'

# Opening the browser with the link and the arguments passed
webbrowser.open(link+''+address)

