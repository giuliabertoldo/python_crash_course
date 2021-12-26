# 11.1 TESTING A FUNCTION
## EXERCISE 11-1

import unittest
from city_functions import city_country

class tests_city(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        """Do inputs like "rome" "italy" work?"""
        complete_city = city_country('rome', 'italy')
        self.assertEqual(complete_city, "Rome, Italy")

    def test_city_contry_population(self):
        """Do inputs like "santiago", "chile" "5000000" work?"""
        complete_city = city_country('santiago', 'chile', 5000000)
        self.assertEqual(complete_city, "Santiago, Chile - Population: 5000000")

if __name__ == '__main__':
    unittest.main()
