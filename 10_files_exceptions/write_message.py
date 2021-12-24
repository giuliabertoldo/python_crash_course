# 10.2 WRITING TO A FILE

import os.path

script_path = os.path.dirname(__file__)
filename = os.path.join(script_path, 'programming.txt')

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename) as file_object:
    print(file_object.read())
