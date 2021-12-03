# 3.2 CHANGING, ADDING, AND REMOVING ELEMENTS
## EXERCISE 3-5

guests = ['Alice', 'Bob', 'Charlie']
print(guests)

message1 = f"{guests[0]} can't make it!"
print(message1)

guests.remove('Alice')
print(guests)
guests.insert(0, 'Dan')
print(guests)

message = f"Hi {guests[0]}! Would you like to come to dinner?"
print (message)

message = f"Hi {guests[1]}! Would you like to come to dinner?"
print (message)

message = f"Hi {guests[2]}! Would you like to come to dinner?"
print (message)
