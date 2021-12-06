# 7.3 USING A WHILE LOOP WITH LISTS AND DICTIONARIES
## PAG. 124

unconfirmed_users = ['Alice', 'Bob', 'Charlie']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user}")
    confirmed_users.append(current_user)


print("Verification process complete.")
print("The verified users are:")
for user in confirmed_users:
    print(user)
