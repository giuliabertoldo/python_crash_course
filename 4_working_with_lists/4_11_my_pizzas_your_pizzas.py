# 4.4 WORKING WITH PART OF A LIST
## EXERCISE 4-11

pizzas = ['margherita', 'bufalina', 'primavera']
print(pizzas)

friend_pizzas = pizzas[:]
print(friend_pizzas)

pizzas.append('quattro stagioni')
print(pizzas)

friend_pizzas.append('calzone')
print(friend_pizzas)

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizas are:")
for pizza in friend_pizzas:
    print(pizza) 
