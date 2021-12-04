# 6.4 NESTING
## EXERCISE 6-6

person1 = {
    'first_name' : 'Alice',
    'last_name': 'Smith',
    'age': 30,
    'city': 'San Francisco'
    }

person2 = {
    'first_name' : 'Bob',
    'last_name': 'Brown',
    'age': 20,
    'city': 'Los Angeles'
    }

person3 = {
    'first_name' : 'Charlie',
    'last_name': 'Jones',
    'age': 50,
    'city': 'San Diego'
    }

people = [person1, person2, person3]

for person in people:
    print(person)
