# 10.3 EXCEPTIONS
## EXERCISE 10-9

import os.path
script_path = os.path.dirname(__file__)
file_name1 = os.path.join(script_path, 'cats.txt')
file_name2 = os.path.join(script_path, 'dogs.txt')

animals= [file_name1, 'dogs.txt']

for animal in animals:
    try:
        with open(animal) as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        print(content)
