# 5. IF STATEMENTS
## CHAPTER NOTES
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

car = 'bmw' # Assignment
print(car == 'bmw') # Equality conditional test

print(car.lower() == 'bmw')
print(car.lower() != 'bmw')

car = 'audi'
if (car.lower() != 'bmw'):
    print (f"The car is not a bmw, it is {car}")

age_0 = 27
age_1 = 31
print((age_0 >= 30) and (age_1 > 30))
print((age_0 >= 30) or (age_1 > 30))# True

print('\n')
fruits = ['apple','peach', 'banana']
print('apple' in fruits) # True
print('tomato' not in fruits)

print('\n')
# 5.3 USING IF STATEMENTS WITH LISTS

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping.lower() == 'green peppers':
        print('Sorry, we are out of green peppers right now')
    else:
        print(f'Adding {requested_topping}')

print('\n')

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping.lower() == 'green peppers':
            print('Sorry, we are out of green peppers right now')
        else:
            print(f'Adding {requested_topping}')
else:
    print("Are you sure you want a plain pizza?")

print('\n')
available_toppings = ['mushrooms', 'olives', 'green_peppers']
requested_toppings = ['pineapple', 'olives']

for topping in requested_toppings:
    if topping not in available_toppings:
        print(f"Sorry, we don't have {topping}")
    else:
        print(f"{topping} added to pizza")
