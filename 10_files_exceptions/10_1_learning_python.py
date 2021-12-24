# 10.1 FILES AND EXCEPTIONS
# EXERCISE 10-1

import os.path
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'learning_python.txt')

# Read the entire file
with open(filename) as file_object:
    contents = file_object.read()
print(contents.strip())

print('\n Next')
# Loop over the file file_object
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Store lines in a list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
