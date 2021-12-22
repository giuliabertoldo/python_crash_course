# 9.5 PYTHON STANDARD LIBRARY
## EXERCISE 9-15

from random import choice

my_ticket = 1
print(my_ticket)

numbers = list(range(1,11))
letters = ["a", "b", "c", "d", "e"]
list1 = numbers + letters

winner = choice(list1)
count = 0

while my_ticket != winner:
    winner = choice(list1)
    print("You are not a winner.")
    count += 1

print(f"You won at the {count} time.")
