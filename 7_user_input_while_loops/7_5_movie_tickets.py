# 7.2 INTRODUCING WHILE LOOPS
## EXERCISE 7-5

prompt = "\nWhat is your age? "
prompt += "\n(type 'quit' when you are finished) "

active = True

while active == True:
    ticket = input(prompt)

    if ticket == "quit":
        break

    ticket = int(ticket)
    if ticket < 3:
        print("The ticket is free")
    elif (ticket >= 3) and (ticket < 12):
        print("The ticket costs $10")
    elif(ticket >= 12):
        print("The ticket costs $15")
