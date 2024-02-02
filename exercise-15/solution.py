# Solution to Exercise 15 (Main Problem)

def get_rainfall():

    rainfall_dict = dict()

    while city := input("Please enter a city: "):

        rain_inches = int(input(f"How much rainfall (in mm) has {city} encountered? "))

        rainfall_dict[city] = rainfall_dict.get(city, 0) + rain_inches
    
    if len(rainfall_dict) > 0:

        for city, rain in rainfall_dict.items():

            print(f"{city} received {rain} inches of rainfall.")


get_rainfall()
