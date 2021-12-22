#  9.2 WORKING WITH CLASSES AND INSTANCES
## EXERCISE 9-5

class Users:
    """Modelling user profile"""
    def __init__(self, name, surname, age, gender, login_attempts):
        self.first_name = name
        self.last_name = surname
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"The user's name is {self.first_name}")
        print(f"The user's surnmae is {self.last_name}")
        print(f"The user's age is {self.age}")
        print(f"The user's gender is {self.gender}")

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = Users("Alice", "Smith", "20", "Female", 40)

times = list(range(1,10))
print(times)

for time in times:
    user1.increment_login_attempts()
    print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
