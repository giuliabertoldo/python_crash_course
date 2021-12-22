# 9.3 INHERITANCE
## EXERCISE 9-6

class Restaurant:
    """A model for restaurants."""

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

class IceCreamStand(Restaurant):
    """A model of an Ice Cream Stand."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """
        Initialize attributes of the parent class.
        Then, initialize specific attributes.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"The requested flavors are: {self.flavors}")

stand1 = IceCreamStand("Name", "Gelato", "Banana, Chocolate, Vanilla")
stand1.display_flavors()
