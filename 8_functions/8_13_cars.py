# 8.5 PASSING AN ARBITRARY NUMBER OF ARGUMENTS
## EXERCISE 8-14

def make_car(manufacturer, model, **kwarg):
    """Sotre information about a car"""
    kwarg['manufacturer'] = manufacturer
    kwarg['model'] = model
    return kwarg

car1 = make_car('fiat', 'panda', color = 'blue',
                        tow_package = True)
print(car1)
