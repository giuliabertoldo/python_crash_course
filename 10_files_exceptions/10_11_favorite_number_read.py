# 10.4 STORING DATA

import json
import os.path

script_path = os.path.dirname(__file__)
filename = os.path.join(script_path, 'favorite_number.json')

with open(filename) as f:
    number = json.load(f)

print(f"I know your favorite number is {number}!")
