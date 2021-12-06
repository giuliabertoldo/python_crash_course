# 7.3 USING A WHILE LOOP WITH LISTS AND DICTIONARIES
## EXERCISE 7-10

prompt1 = "\nWhat is your name? "

prompt2 = f"\nIf you could visit one place in the world,"
prompt2 += "where would you go? "

prompt3 = "\nWould you like anybody else to fill in the poll? (yes/no) "

vacation = {}
active = True

while active == True:
    name = input(prompt1)
    place = input(prompt2)
    status = input(prompt3)

    vacation[name] = place

    if status == 'no':
        active = False

print("\n--- Poll results ---")
for name, place in vacation.items():
    print(f"{name} would like to visit {place}.")
