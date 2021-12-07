#8.3 RETURN VALUES
## EXERCISE 8-6

def city_country(city, country):
    """Return city country pairs, neatly formatted"""
    pair = f"{city.title()}, {country.title()}"
    return pair

first = city_country('Amsterdam', 'The Netherlands')
print(first)

second = city_country('Rome', 'Italy')
print(second)

third = city_country('Paris', 'France')
print(third)
