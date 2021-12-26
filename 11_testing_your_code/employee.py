# 11.2 TESTING A CLASS
## EXERCISE 11-3

class Employee:
    """Model employee"""

    def __init__(self, name, last_name, an_salary):
        """Initialize attributes"""
        self.name = name
        self.last_name = last_name
        self.an_salary = an_salary

    def give_raise(self, up = 5000):
        new_salary = self.an_salary + up
        return(new_salary)
