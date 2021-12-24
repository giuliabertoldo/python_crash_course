# 10.4 STORING DATA
## EXERCISE 10-4

import json
import os.path

script_path = os.path.dirname(__file__)
filename = os.path.join(script_path, 'fav_number.json')

try:
    with open(filename) as f:
        answer = json.load(f)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    print(f"Your favorite number is {favorite_number}!!")
else:
    print(f"Your favorite number is {answer}!")
