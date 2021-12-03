# 3.2 CHANGING, ADDING, AND REMOVING ELEMENTS
## EXERCISE 3-7

guests = ['Eve', 'Dan', 'Frank', 'Bob', 'Charlie', 'Grace']
print(guests)

message1 = "Hi guys! I can only invite two people for dinner."
print(message1)

removed_guest = guests.pop()
message2 = f"Hi {removed_guest}! I am sorry but I can't invite you to dinner."
print(message2)
print(guests)

removed_guest = guests.pop()
message2 = f"Hi {removed_guest}! I am sorry but I can't invite you to dinner."
print(message2)
print(guests)

removed_guest = guests.pop()
message2 = f"Hi {removed_guest}! I am sorry but I can't invite you to dinner."
print(message2)
print(guests)

removed_guest = guests.pop()
message2 = f"Hi {removed_guest}! I am sorry but I can't invite you to dinner."
print(message2)
print(guests)

message3 = f"Hi {guests[0]}! I am happy to invite you to dinner."
print(message3)

message3 = f"Hi {guests[1]}! I am happy to invite you to dinner."
print(message3)

del(guests[0])
del(guests[0])
print(guests)
