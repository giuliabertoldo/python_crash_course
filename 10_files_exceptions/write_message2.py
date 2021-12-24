# 10.2 WRITING TO A FILE

import os.path
script_path = os.path.dirname(__file__)
filename = os.path.join(script_path, 'programming.txt')

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser. \n")

with open(filename) as file_object:
    print(file_object.read())

'r'
