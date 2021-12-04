# 6.2 WORKING WITH DICTIONARIES
## EXERCISE 6-5

rivers = {
    'Willamette' : 'Oregon',
    'Yellowstone' : 'North Dakota',
    'Yukon' : 'Alaska',
    }

for river, state in rivers.items():
    print(f"The {river} runs through {state}.")

for river in rivers.keys():
    print(river)

for state in rivers.values():
    print(state)
