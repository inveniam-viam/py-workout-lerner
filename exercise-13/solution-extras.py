# Solutions to Additional Problems - Exercise 13

from operator import itemgetter, attrgetter
from collections import namedtuple

# Exercise 13.1

person = namedtuple("Person", ["LastName", "FirstName", "Time"])

xi = person("Xi", "Jinping", 10.603)
donny = person("Trump", "Donald", 7.85)
vlad = person("Putin", "Vladimir", 3.626)

peoples = [xi, donny, vlad]

def format_sort_records(input_seq: list) -> list[str]:

    """Solving Exercise 13 but with namedtuples"""

    out_list: list[str] = []

    template = "{0:10}{1:10}{2:5.2f}"

    for individual in sorted(input_seq, key = attrgetter("LastName", "FirstName")):

        out_list.append(template.format(*individual))
    
    return out_list


# Testing 13.1
print('\n'.join(format_sort_records(peoples)))



# Exercise 13.2

movies: list[tuple] = [
    ("The Shape of Water", 123, "Guillermo del Toro"),
    ("Moonlight", 111, "Barry Jenkins"),
    ("La La Land", 128, "Damien Chazelle"),
    ("Green Book", 130, "Peter Farrelly"),
    ("Parasite", 132, "Bong Joon-ho")
]

def sort_by_user_choice(selection: int) -> list[str]:

    """Function that sorts a list of tuples containing movie info
    according to the user's choice of sort axis (title / minutes / director)"""

    out_list: list[str] = []

    movies_sorted = sorted(movies, key = itemgetter(selection))

    template = "{0:30} {2:20} {1:5}"

    for movie in movies_sorted:
        # when you send *movie, you get to unpack the tuple into
        # its individual components and thereby easily toss it into the formatter
        out_list.append(template.format(*movie))

    return out_list

# Testing 13.2 solution


# user_choice : int= int(input("Please enter a choice to sort by: \n 0. Title \n 1. Runtime \n 2. Director "))

# print('\n'.join(sort_by_user_choice(user_choice)))


# 13.2 -- Kinda same as 13.3 but with 2 or 3 choices 

movies: list[tuple] = [
    ("The Shape of Water", 123, "Guillermo del Toro"),
    ("Moonlight", 111, "Barry Jenkins"),
    ("La La Land", 128, "Damien Chazelle"),
    ("Green Book", 130, "Peter Farrelly"),
    ("Parasite", 132, "Bong Joon-ho")
]

def sort_by_axis(in_seq: list, *args) -> list:

    """Implementing 13.1 but with more complexity in user choices for axes"""
    
    out_list: list =[]

    template = "{0:25}{2:25}{1:15}"

    for movie in sorted(in_seq, key = itemgetter(*args)):

        out_list.append(template.format(*movie))

    return out_list

user_choice = input("Please enter one or more choices to sort by: \n 0. Title \n 1. Runtime \n 2. Director ")

user_choice = [int(x) for x in user_choice.split()]


print('\n'.join(sort_by_axis(movies, *user_choice)))
