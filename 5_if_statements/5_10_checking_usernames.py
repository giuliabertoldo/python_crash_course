# 5.3 USING IF STATEMENTS WITH LISTS
## EXERCISE 5-10

current_users = ['Admin', 'Alice', 'Bob', 'Charlie', 'Dan']

lower_current_users

new_users = ['alice', 'Bob', 'Eve', 'Grace']

for user in new_users:
    if user.title() in current_users:
        print("Username not available")
    else:
        print("Username available")
