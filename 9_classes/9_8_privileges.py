# 9.3 INHERITANCE
## EXERCISE 9-8

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

class Privileges():
    """Model privileges."""

    def __init__(self, privileges = ["Can add post", "Can delete post"]):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"{privilege}")

class Admin(Users):
    """Model Admin"""

    def __init__(self, name, surname, age, gender, login_attempts):
        """
        Initialize parent attributes.
        Then initialize specific attributes.
        """
        super().__init__(name, surname, age, gender, login_attempts)
        self.privileges = Privileges()

admin1 = Admin("G", "B", "20", "F", 40)
admin1.privileges.show_privileges()
