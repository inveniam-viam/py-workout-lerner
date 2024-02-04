# Solution to Additional Problems

# 16.1 - Merge Dictionaries

def merge_dicts(*args) -> dict:

    """Takes any number of dicts and returns a dict
    that reflects the combination of all of them.
    If same key appears more than once, most recent
    value is the final value."""

    output_dict: dict = {}

    for dct in args:

        for key, val in dct.items():

            output_dict[key] = val

    return output_dict

# 16.1 Alternative

def better_merge_dicts(*dicts) -> dict:

    """Cleaner, less clunky version of the former impl."""

    output_dict: dict = {}

    for dct in dicts:

        output_dict.update(dct)
    
    return output_dict


# 16.2

def dict_from_evens(*args) -> dict:

    output_dict = dict()

    counter: int = 0

    while len(args) % 2 == 0 and counter < len(args):

        output_dict[args[counter]] = args[counter + 1]

        counter += 2
    
    return output_dict
