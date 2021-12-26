# 11.2 TESTING A CLASS
## EXERCISE 11-3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """
        Create an employee
        """
        name = "Alice"
        last_name = "Smith"
        an_salary = 100000
        self.employee1 = Employee(name, last_name, an_salary)

    def test_give_default_raise(self):
        """Test that a default raise is properly given."""
        total = self.employee1.give_raise()
        self.assertEqual(total, 105000)

    def test_give_custome_raise(self):
        """Test that a custom raise is properly given."""
        total = self.employee1.give_raise(up = 2000)
        self.assertEqual(total, 102000)

if __name__ == '__main__':
    unittest.main()
