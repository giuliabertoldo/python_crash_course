# 9.1 CREATING AND USING CLASSES
## EXERCISE 9-2

class Restaurant:
    """A model for restaurants"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open!")

# Instance 1
res1 = Restaurant("Alice", "American")
res1.describe_restaurant()

# Instance 2
res2 = Restaurant("Bob", "Bulgarian")
res2.describe_restaurant()

# Instance 3
res3 = Restaurant("Charlie", "Chinese")
res3.describe_restaurant()
