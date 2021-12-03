# 3. INTRODUCING LISTS
## My notes and examples

# 3.1 WHAT IS A LIST?
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars[0])
print(cars[-1])

print(cars[0].upper())

message = f"My first car was a {cars[0]}."
print(message)

# 3.2 CHANGING, ADDING AND REMOVING ELEMENTS
cars[0] = "abarth"
print(cars)

cars.append('bmw')
print(cars)

cars.insert(1,'lancia')
print(cars)

del(cars[0])
print(cars)


popped_cars1 = cars.pop()
print(popped_cars1)

popped_cars2 = cars.pop(0)
print(popped_cars2)

cars.remove("toyota")
print(cars)

too_expensive = "audi"
cars.remove(too_expensive)
print(cars)
print(f"\nA {too_expensive} is too expensive for me.")

# 3.3 ORGANIZING A LIST
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

print("\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

print("\n")

print(sorted(cars))
print(cars)

cars = ['bmw', 'audi', 'Toyota', 'Subaru']
print(sorted(cars))

print(cars)
print(cars.reverse())
print(cars)
print(len(cars))
