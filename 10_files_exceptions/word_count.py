# 10.3 EXCEPTIONS

def count_words(file_name, file_path):
    """Count the approximate number of words in a file."""
    try:
        with open(file_path, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does no exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")


import os.path
script_path = os.path.dirname(__file__)
file_name = 'alice.txt'
file_path = os.path.join(script_path, file_name)

count_words(file_name, file_path)
