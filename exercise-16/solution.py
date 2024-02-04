from collections import defaultdict

def dictdiff(dict1, dict2) -> dict:

    """Function that returns the difference between two dictionaries"""

    dict_diffs = defaultdict(list)

    all_keys: set = dict1.keys() | dict2.keys()

    for key in all_keys:

        if dict1.get(key) != dict2.get(key):

            dict_diffs[key].extend([dict1.get(key), dict2.get(key)])
    
    return dict(dict_diffs)

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d1, d1))
print(dictdiff(d1, d2))
 
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d3, d4))
 
d5 = {'a':1, 'b':2, 'd':4}
print(dictdiff(d1, d5))
