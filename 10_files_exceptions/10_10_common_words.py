# 10.3 EXCEPTIONS
## EXERCISE 10-10

import os.path
script_path = os.path.dirname(__file__)
file_name1 = 'psychology_and_achievemnt.txt'
file_name2 = 'increasing_human_efficiency.txt'
file_name3 = 'increasing_personal_efficiency.txt'
file_path1 = os.path.join(script_path, file_name1)
file_path2 = os.path.join(script_path, file_name2)
file_path3 = os.path.join(script_path, file_name3)

files = [file_path1, file_path2, file_path3]


for file in files:
    with open(file) as f:
        content = f.read()
        words = content.split()
        num_words = len(words)
        words_the = content.lower().count('the')
        words_the_space = content.lower().count('the ')
        print(f"In this file 'the' appers {words_the} times and 'the + space' {words_the_space} times. ")
