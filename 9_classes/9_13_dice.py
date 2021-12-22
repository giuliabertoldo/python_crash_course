# 9.5 PYTHON STANDARD LIBRARY
## EXERCISE 9-13

from random import randint

class Die():
    """Model of a die."""

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))

die1 = Die()
die1.roll_die()

print('\n')

die2 = Die(sides = 10)
times = range(1,10)
for time in times:
    die2.roll_die()

print('\n')

die3 = Die(sides = 20)
times = range(1,10)
for time in times:
    die2.roll_die()
