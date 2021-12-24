# 10.2 WRITING TO A FILE
filename = 'guest_book.txt'

prompt = "\nWhat is your name? "
prompt += "\nEnter 'quit' to end the program. "

name = ""
while name != "quit":
    name = input(prompt)
    if name != "quit":
        print(f"Hi {name}! ")
        with open(filename, 'a') as file_object:
            file_object.write(f"{name} \n")
