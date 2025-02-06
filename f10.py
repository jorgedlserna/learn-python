import os, shutil

# Combining 3 folders and a file into a path
print(os.path.join('folder1','folder2','folder3','file.png'))

# Returning the abs path of currect working directoy
print(os.getcwdb())

# Changing the current directory to the parent directory
os.chdir('..')
print(os.getcwdb())

os.chdir('learn-python')
print(os.getcwdb())

# Returning the abs path of the path passed to it
print(os.path.abspath('f10.py'))

# Checking if the path passed is an absolute path
print(os.path.isabs('c:/folder1/folder2')) # True
print(os.path.isabs('../')) # False

# Returning the rel path of the two paths passed
print(os.path.relpath('c:/folder1/folder2/folder3/file.png', 'c:/folder1/folder2'))

# Checking if the path passed exists
print(os.path.exists('c:/folder1/folder2')) # False
print(os.path.exists('c:/Users')) # True

# Checking if the path passed is a file
print(os.path.isfile('./f10.py')) # True
print(os.path.isdir('c:/folder1/folder2')) # False

totalSize=0
# Returning all the files and directories within the path passed
for filename in os.listdir('./'):
    # If path passed is not a file, then continue
    if not os.path.isfile(os.path.join(os.getcwd(), filename)):
        continue
    # Summing the size of the file of the path passed to a variable
    totalSize=totalSize+os.path.getsize(os.path.join(os.getcwd(), filename))
# Printing the totalsize of the files in the path passed
print(totalSize)

# Creating a directory
os.makedirs('/test')

# Opening a file
helloFile=open('hello.txt')

# Reading its content
content=helloFile.read()
print(content)

# Closing a file
helloFile.close()

# Opening a file in writable mode
helloFile=open('hello.txt', 'w')

# Replacing the content of the file with the string passed
helloFile.write('Adding some text to hello.txt')
helloFile.close()

# Adding content to the file
helloFile=open('hello.txt', 'a')
helloFile.write('\n\nAdding some text to hello.txt')
helloFile.close()

# Copying the file hello.txt to the path passed
shutil.copy('hello.txt', 'c:/Users/jorge')

# Copying an entire directory to the path passed
shutil.copytree('..', 'c:/Users/jorge')

# Moving a file to the path passed
shutil.move('hello.txt', 'c:/Users')

# Deleting a file
os.unlink('hello.txt')

# Deleting an empty directory
os.rmdir('c:/Users/jorge')

# Deleting a directory permanently
shutil.rmtree('test/')