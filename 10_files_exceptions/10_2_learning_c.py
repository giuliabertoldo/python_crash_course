# 10.1 FILES AND EXCEPTIONS
# EXERCISE 10-2

import os.path
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'learning_python.txt')

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'R'))





print('\n')

message = "I really like dogs."
print(message)

print(message.replace('dog', 'cat'))
