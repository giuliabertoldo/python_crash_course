"""A set of classes tha can be used to represent admins"""

from user1 import Users

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
