# 6.2 WORKING WITH DICTIONARIES
## EXERCISE 6-2

favorite_numbers = {
    'alice' : '1',
    'bob' : '2',
    'charlie' : '3',
    'dan' : '4',
    'eve' : '5'
    }

print('\n')
names = ['alice', 'bob', 'charlie', 'dan', 'eve']
for name in names:
    number = favorite_numbers[name]
    print(f"{name}'s favorite number is {number}")

####### PREVIOUS CODE #######
number = favorite_numbers['alice']
print(f"Alice's favorite number is {number}")

name = 'bob'
number = favorite_numbers[name]
print(f"{name}'s favorite number is {number}")

name = 'charlie'
number = favorite_numbers[name]
print(f"{name}'s favorite number is {number}")

name = 'dan'
number = favorite_numbers[name]
print(f"{name}'s favorite number is {number}")

name = 'eve'
number = favorite_numbers[name]
print(f"{name}'s favorite number is {number}")
