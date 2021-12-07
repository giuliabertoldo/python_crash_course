# 8.5 PASSING AN ARBITRARY NUMBER OF ARGUMENTS
## PAG. 147

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')

make_pizza(12, 'pepperoni', 'mushrooms', 'extra cheese')
