# 9.1 CREATING AND USING CLASSES
## EXERCISE 9-3

class Users:
    """Modelling user profile"""
    def __init__(self, name, surname, age, gender):
        self.first_name = name
        self.last_name = surname
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"The user's name is {self.first_name}")
        print(f"The user's surnmae is {self.last_name}")
        print(f"The user's age is {self.age}")
        print(f"The user's gender is {self.gender}")

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}!")

user1 = Users("Alice", "Smith", 28, "Female")
user1.describe_user()
user1.greet_user()
