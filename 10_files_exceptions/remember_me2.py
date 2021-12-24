# 10.4 STORING DATA

import json
import os.path

def greet_user():
    """Greet the user by name"""
    script_path = os.path.dirname(__file__)
    filename = os.path.join(script_path, 'username.json')

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dumpt(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()


def get_stored_useraname():
    """Get stored username if available."""
    script_path = os.path.dirname(__file__)
    filename = os.path.join(script_path, 'username.json')
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    script_path = os.path.dirname(__file__)
    filename = os.path.join(script_path, 'username.json')
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_useraname()
    if username:
        print(f"Welcome back, {username}!")
    else:
        get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
