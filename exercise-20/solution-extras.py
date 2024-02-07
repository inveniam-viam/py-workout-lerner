# Solutions to additional problems from exercise 20

import os
import glob
from collections import Counter

def selected_wcs() -> dict:

    """Ask the user to enter the name of a text file and then (on one line, separated by spaces)
    words whose frequencies should be counted in that file. Count how many times those words appear in a dict, 
    using the user-entered words as the keys and the counts as the values."""
    in_line = input("Please enter a .txt file separated by words in spaces on the same line: ")

    out_dict: dict= {}

    if in_line:

        in_split: list = in_line.split()

        in_file: str = in_split[0]

        selected_words = in_split[1:]

        out_dict: dict = dict.fromkeys(selected_words, 0)

        with open(in_file, "r", encoding = "utf-8") as f:

            for line in f:

                for word in line.split():

                    if word in out_dict:

                        out_dict[word] += 1

    return out_dict

# 20.2

def return_filesizes():

    """Create a dictionary with the filename and its size for all files in a given folder."""

    output_dict: dict = {}

    for file in os.listdir():

        output_dict[file] = os.stat(file).st_size
    
    return output_dict


# 20.3

def popular_letters(dirname: str):

    out_dict = Counter()

    for filename in glob.glob(f"{dirname}/*.txt"):

        try:

            with open(filename, "r", encoding = "utf-8") as f:

                for line in f:


                    out_dict.update(Counter(line.strip()))
        except: 

            pass
    
    return list(dict(out_dict.most_common(5)).keys())


print(popular_letters("/Users/jarwind/Work/python-rushmore/reuven-lerner/py-workout-lerner/exercise-20/"))
