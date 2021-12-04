# 6. DICTIONARIES
## NOTES

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


alien_0['color'] = 'green'
alien_0['points'] = '5'
print(alien_0)

alien_0['color'] = 'yellow'
print(alien_0)

del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    }
print(favorite_languages)

# favorite_languages['giulia']
print(favorite_languages.get('giulia'))
print(favorite_languages.get('giulia', 'No language assigned'))

print(favorite_languages.items())

for name, language in favorite_languages.items():
    print(f"\nName: {name}")
    print(f"Language: {language}")


for name, language in favorite_languages.items():
    print(f"\nName: {name}'s favorite language is {language}.")


alien_0 = {'color': 'green', 'points': 5}
for key, value in alien_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for name in favorite_languages.keys():
    print(f"{name} took part at the poll.")

print('\n')
for name in favorite_languages:
    print(f"{name} took part at the poll.")

if 'jen' in favorite_languages.keys():
    print("Jen took the poll")

for name in sorted(favorite_languages.keys()):
    print(f"{name}, thank you for taking the poll")

for language in favorite_languages.values():
    print(language)

languages = {'python', 'c', 'ruby'}
print(languages)

print('\n')

user1 = {
    'name' : 'Alice',
    'number' : 1,
    }

user2 = {
    'name' : 'Bob',
    'number' : 2,
    }

user3 = {
    'name' : 'Charlie',
    'number' : 3,
    }

users = [user1, user2, user3]

for user in users:
    print(user)

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
    }

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

print('\n')

favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    }
for name, languages in favorite_languages.items():
    print(f"{name}'s favorite languages are:")
    for language in languages:
        print(f"{language}")

print('\n')

users = {
    'aeinstein' : {
        'first': 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
        },
    'mcurie' : {
        'first': 'marie',
        'last' : 'curie',
        'location' : 'paris',
        },

    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")

    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\t Full name: {full_name}")
    print(f"\t Location: {location}")
