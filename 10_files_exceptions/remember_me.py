# 10.4 STORING DATA

import os.path
import json

username = input('What is your name? ')

script_path = os.path.dirname(__file__)
filename = os.path.join(script_path, 'username.json')

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")
