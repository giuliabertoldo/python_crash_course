# 6.2 WORKING WITH DICTIONARIES
## EXERCISE 6-6

people = ['jen', 'sarah', 'edward', 'alice', 'bob']

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    }

for person in people:
    done = favorite_languages.keys()
    if person in done:
        print(f"Thank you {person}!")
    else:
        print(f"{person}, would you like to take the poll?")
