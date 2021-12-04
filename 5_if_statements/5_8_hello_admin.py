# 5.3 USING IF STATEMENTS WITH LISTS
## EXERCISE 5-8

users = ['admin', 'Alice', 'Bob', 'Charlie', 'Dan']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
