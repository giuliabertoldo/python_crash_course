# 9.5 PYTHON STANDARD LIBRARY
## EXERCISE 9-14

from random import choice

numbers = list(range(1,11))
letters = ["a", "b", "c", "d", "e"]
print(numbers)
print(letters)
list1 = numbers + letters

winners = []
for i in range(1,5):
    winner = choice(list1)
    winners.append(winner)

print("The winners are:")
for w in winners:
    print(w)
