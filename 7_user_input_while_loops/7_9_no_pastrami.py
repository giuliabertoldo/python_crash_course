# 7.3 USING A WHILE LOOP WITH LISTS AND DICTIONARIES
## EXERCISE 7-9

sandwich_orders = ['submarine', 'pastrami', 'New York special', 'pastrami',  'vegetarian', 'pastrami']

finished_sandwiches = []

while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        print("Deli has ran out of pastrami." )
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("I made these sanwiches:")
for f in finished_sandwiches:
    print(f)
