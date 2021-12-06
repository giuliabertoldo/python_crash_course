# 7. USER INPUT AND WHILE LOOPS
## PAG. 121

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(enter 'quit' when you are finished) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city}!")
