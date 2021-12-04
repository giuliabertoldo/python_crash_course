# 4. WORKING WITH LISTS
## NOTES

# 4.1 LOOPING THROUGH AN ENTIRE LIST
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 4.3 MAKING NUMERICAL LISTS
for value in range(1,5):
    print(value)

numbers = range(1,6)
print(numbers)

numbers = list(range(1,6))
print(numbers)

print(list(range(6)))

print(list(range(1,6,2)))

squares = [ ]
for value in range(0, 11):
    square = value**2
    squares.append(square)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)

print(digits)
print(digits[0:3])

print(digits[:3])
print(digits[0:])
print(digits[-3:])
print(digits[:5: 2])

for digit in digits[:6:2]:
    print(f"{digit} is an odd number")

foods = ["pasta", "pizza", "gelato"]
friend_foods = foods[:]
friend_foods.append('sandwich')
print(foods)
print(friend_foods)

my_friend_foods = foods
print(my_friend_foods)
print(foods)
foods.append('cannoli')
print(my_friend_foods)


dimensions = (200, 50)
print(dimensions)

print(dimensions[0])

my_tuple = (3, )
print(my_tuple)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 40)
print("New dimensions:")
for dimension in dimensions:
    print(dimension)
