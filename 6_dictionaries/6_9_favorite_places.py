# 6.4 NESTING
## EXERCISE 6-9

favorite_places = {
    'alice' : ['milan'],
    'bob' : ['rome', 'milan'],
    'charlie' : ['san diego'],
    }

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()} favorite place is:")
        for p in places:
            print(f"{p}")
    else:
        print(f"\n{name.title()} favorite places are:")
        for p in places:
            print(f"{p}")
