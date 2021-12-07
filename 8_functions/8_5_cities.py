# 8.2 PASSING ARGUMENTS
## EXERCISE 8-5

def describe_city(city, country = 'Italy'):
    print(f"{city.title()} is in {country.title()}.")

describe_city(city = 'Rome')
describe_city(city = 'Amsterdam', country = 'The Netherlands')
describe_city(city = 'Los Angeles', country = 'United States')
