# 6.4 NESTING
## EXERCISE 6-10

favorite_numbers = {
    'alice' : ['1', '11'],
    'bob' : ['2','22'],
    'charlie' : ['3'],
    'dan' : ['4', '44'],
    'eve' : ['5']
    }

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{name.title()}'s favorite number is:")
        for number in numbers:
            print(number)
    else:
        print(f"{name.title()}'s favorite numbers are:")
        for number in numbers:
            print(number)
