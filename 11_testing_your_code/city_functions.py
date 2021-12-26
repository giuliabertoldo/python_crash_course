# 11.1 TESTING A FUNCTION
## EXERCISE 11-1

def city_country(city, country, population = ''):
    if population:
        full_city = f"{city}, {country} - population: {population}"
    else:
        full_city = f"{city}, {country}"
    return(full_city.title())
