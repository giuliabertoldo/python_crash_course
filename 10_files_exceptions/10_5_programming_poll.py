# 10.2 WRITING TO A FILE

prompt = "Why do you like programming? \n"
prompt += "Type 'quit' to exit."

reason = ""

while reason != 'quit':
    reason = input(prompt)
    with open('responses.txt', 'a') as object_file:
        object_file.write(f"{reason} \n")
