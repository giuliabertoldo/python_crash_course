# 10.4 STORING DATA
## EXERCISE 10-11

import json
import os.path

script_path = os.path.dirname(__file__)
filename = os.path.join(script_path, 'favorite_number.json')

fav_num = input("What is your favorite number? ")

with open(filename, 'w') as f:
    json.dump(fav_num, f)
