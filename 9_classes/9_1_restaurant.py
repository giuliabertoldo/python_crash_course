# 9.1 CREATING AND USING CLASSES
## EXERCISE 9-1

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
restaurant = Restaurant("Tony", "Italian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
