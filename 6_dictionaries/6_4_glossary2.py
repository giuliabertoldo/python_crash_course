# 6.2 WORKING WITH DICTIONARIES
## EXERCISE 6-4

glossary = {
    'Dictionary': 'a collection of key-value pairs',
    'Key-value pair' : 'a set of values associated with each other',
    'Boolean expression' : 'another name for conditional test',
    'Conditional test' : 'an expression that can be evaluated as true or false',
    'Tuple' : 'immutable list',
    'List' : 'a dynamic collection of items in a particular order',
    }

for k, v in glossary.items():
    print(f"\n{k}: {v}.")
