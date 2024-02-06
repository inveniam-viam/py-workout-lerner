# Solution to additional problems from Exercise 19
from collections import defaultdict

# 19.1 - Implementation using defaultdict

def shell_user_info(in_filepath: str) -> dict:

    output_dict = defaultdict(list)

    with open(in_filepath, "r", encoding = "utf-8") as file:

        for line in file:

            line = line.strip()

            if not line.startswith(("#", "\n")):

                shell = line.split(":")[-1]

                user = line.split(":")[0]

                output_dict[shell].append(user)
    
    return dict(output_dict)

# 19.1 - Implementation without defaultdict

def alt_shell_user_info(in_filepath: str) -> dict:

    output_dict:dict = {}

    with open(in_filepath, "r", encoding = "utf-8") as file:

        for line in file:

            if not line.startswith(("#", "\n")):

                line = line.strip()

                shell = line.split(":")[-1]
                user = line.split(":")[0]

                if shell in output_dict:

                    output_dict[shell].append(user)
                
                else:

                    output_dict[shell] = [user]
    
    return output_dict


# 19.2 

# the most annoying problem tbh

def helper_factors(n):

    """Find the factors of a given number. Helper function."""

    factors_n = set()

    for i in range(1, n):

        if n % i == 0:

            factors_n.add(i)
    
    return factors_n

def factor_exercise(in_str):

    """Does whatever weird contraption that the question asked for."""

    out_dict = defaultdict(list)

    numbers: list = [int(element) for element in in_str.split() if element.isdigit()]

    element_factors: set = set(numbers)

    for number in numbers:

        element_factors = element_factors.union(helper_factors(number))
    
    for number in element_factors:

        for num in numbers:

            if (num % number) == 0:

                out_dict[number].append(num)
    
    return out_dict


# 16.3

def passwd_to_user(in_filepath: str) -> dict:

    out_dict: dict = {}

    with open(in_filepath, "r", encoding = "utf-8") as f:

        for line in f:

            if not line.startswith(("#", "\n")):

                particulars = line.split(':')

                username = particulars[0]
                user_id = particulars[2]
                home_dir = particulars[-2]
                shell = particulars[-1]

                out_dict[username] = {"user_id": user_id, "home_dir": home_dir, "shell": shell}
    
    return out_dict


