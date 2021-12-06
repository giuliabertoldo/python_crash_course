# 7.2 INTRODUCING WHILE LOOPS
## EXERCISE 7-4

prompt = "\nWhich pizza toppings would you like? "
prompt += "\n(type 'quit' when you are finished) "

active = True

while active == True:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to the pizza")
