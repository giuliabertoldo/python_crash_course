# 6.4 NESTING
## EXERCISE 6-7

pet1 = {
    'code' : 'id1',
    'kind' : 'cat',
    'owner' : 'alice',
    }
pet2 = {
    'code' : 'id2',
    'kind' : 'dog',
    'owner' : 'bob',
    }
pet3 = {
    'code' : 'id3',
    'kind' : 'bird',
    'owner' : 'charlie',
    }
pet4 = {
    'code' : 'id4',
    'kind' : 'cat',
    'owner' : 'dan',
    }

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print(pet)
