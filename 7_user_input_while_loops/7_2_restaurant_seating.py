# 7.1 HOW THE INPUT() FUNCTION WORKS
## EXERCISE 7-2

people = input("How many people are there in the dinner group? ")
people = int(people)

if people > 8:
    print("You'll have to wait for another table")
else:
    print("Your table is reaady")
