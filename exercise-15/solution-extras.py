# Solutions to additional problems for exercise 15

from collections import defaultdict


# 15.1
def track_rainfall():

    """Calculates the average rainfall (in mm) for a city based on user input."""

    rainfall_dict = {}

    while city := input("Please enter the name of a city: "):

        rainfall_mm = input("Please enter the amount of rainfall (in mm) for the city: ")

        if not rainfall_mm.isdigit():

            print("You entered an invalid input. Please try again.")

        rainfall_mm = int(rainfall_mm)

        if not city in rainfall_dict:

            rainfall_dict[city] = [rainfall_mm]
        else:
            rainfall_dict[city].append(rainfall_mm)

    for city, rain in rainfall_dict.items():

        print(f"The city of {city} received {sum(rain)/len(rain)} millimeters of rain on average.")

# 15.2
def http_response_logger(log_file):

    """Store a list of IP addresses for each HTTP response code seen in a log file from an Apache Server"""

    responses_dict = defaultdict(list)

    with open(log_file, "r", encoding = "utf-8") as f:

        for line in f:

            http_response_code = line.split()[-2]   # standard CLF log file always has status code at this pos
            ip_address = line.split()[0]            # standard CLF log file always has IP address first

            responses_dict[http_response_code].append(ip_address)

    print(dict(responses_dict))

# 15.3
def word_len_counts(file):

    """This function uses a dictionary to track how many words of each length there are in a given file"""

    word_len_dict = {}

    with open(file, 'r', encoding = "utf-8") as f:

        for line in f:

            for word in line.replace('.','').split():

                word_len_dict[len(word)] = word_len_dict.get(len(word), 0) + 1

    print(word_len_dict)

