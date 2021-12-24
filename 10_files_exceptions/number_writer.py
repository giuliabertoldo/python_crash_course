# 10.4 STORING DATA

import os.path
import json

script_path = os.path.dirname(__file__)
filename = os.path.join(script_path, 'numbers.json')

numbers = [2, 3, 5, 7, 11, 13]

with open(filename, 'w') as f:
    json.dump(numbers, f)
