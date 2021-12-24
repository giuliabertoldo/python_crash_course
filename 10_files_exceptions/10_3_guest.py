# 10.2 WRITING TO A FILE

username = input('What is your name? ')

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(username)

with open (filename) as file_object:
    print(file_object.read())
