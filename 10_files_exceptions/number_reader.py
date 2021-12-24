# 10.4 STORING DATA

import os.path
import json

script_path = os.path.dirname(__file__)
filename = os.path.join(script_path, 'numbers.json')

with open(filename) as f:
    numbers = json.load(f)

print(numbers)
