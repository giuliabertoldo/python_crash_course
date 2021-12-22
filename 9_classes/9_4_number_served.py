#  9.2 WORKING WITH CLASSES AND INSTANCES
## EXERCISE 9-4

class Restaurant:
    """A model for restaurants"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open!")

    def increment_number_serveed(self, number):
        self.number_served += number



restaurant = Restaurant("Restaurant1", "Cuisine1")
print(restaurant.number_served)

restaurant.number_served = 10
print(restaurant.number_served)

restaurant.increment_number_serveed(10)
print(restaurant.number_served)
