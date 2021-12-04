# 6.2 WORKING WITH DICTIONARIES
## EXERCISE 6-3

glossary = {
    'Dictionary': 'a collection of key-value pairs',
    'Key-value pair' : 'a set of values associated with each other',
    'Boolean expression' : 'another name for conditional test',
    'Conditional test' : 'an expression that can be evaluated as true or false',
    'Tuple' : 'immutable list',
    'List' : 'a dynamic collection of items in a particular order',
    }

entries = ['Dictionary', 'Key-value pair','Boolean expression',
           'Conditional test', 'Tuple', 'List' ]

for entry in entries:
    definition = glossary[entry]
    print(f"{entry}: {definition} \n")
