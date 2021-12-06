# 7.3 USING A WHILE LOOP WITH LISTS AND DICTIONARIES
## EXERCISE 7-8

sandwich_orders = ['submarine', 'New York special', 'vegetarian']
finished_sandwiches = []


while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("I made these sanwiches:")
for f in finished_sandwiches:
    print(f)
