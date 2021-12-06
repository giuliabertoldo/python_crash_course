# 7.2 INTRODUCING WHILE LOOPS
## EXERCISE 7-7

prompt = "\nWhat is your age? "
prompt += "\n(type 'quit' when you are finished) "

active = True

while active:
    ticket = input(prompt)

    if ticket != 'quit':
        ticket = int(ticket)
        if ticket < 3:
            print("The ticket is free")
        elif (ticket >= 3) and (ticket < 12):
            print("The ticket costs $10")
        elif(ticket >= 12):
            print("The ticket costs $15")
