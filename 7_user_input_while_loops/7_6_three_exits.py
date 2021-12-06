# 7.2 INTRODUCING WHILE LOOPS
## EXERCISE 7-6

# 1
## USE A CONDITIONAL TEST IN THE WHILE STATEMENT TO STOP THE LOOP
prompt = "\nWhat is your age? "
prompt += "\n(type 'quit' when you are finished) "

ticket = ""

while ticket != 'quit':
    ticket = input(prompt)

    if ticket != 'quit':
        ticket = int(ticket)

        if ticket < 3:
            print("The ticket is free")
        elif (ticket >= 3) and (ticket < 12):
            print("The ticket costs $10")
        elif(ticket >= 12):
            print("The ticket costs $15")
