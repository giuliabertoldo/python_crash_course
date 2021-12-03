# 3.3 ORGANIZING A LIST
## EXERCISE 3-10

food = ['sandwich', 'burrito', 'hot dog', 'donut', 'waffles', 'burger']
print(food)

print(food[0])

print(food[-1])

food.append('chicken wings')
print(food)

food.insert(0, 'taco')
print(food)

del(food[0])
print(food)

food.pop()
print(food)

food.pop(1)
print(food)

food.remove("donut")
print(food)

food.sort()
print(food)

food.sort(reverse = True)
print(food)

print(sorted(food))
print(food)

food.reverse()
print(food)

print(len(food))
