# Solution to main problem from exercise 21

import glob

def longest_word(in_file: str) -> str:

    """Returns the longest word in a text file."""

    wordlist = []

    with open(in_file, "r", encoding = "utf-8") as f:

        for line in f:

            line = line.strip()

            for word in line.split():

                wordlist.append(word)
  
    return max(wordlist, key = len)


def longest_words() -> dict:
    
    out_dict: dict = {}

    for file in glob.glob("/Users/jarwind/Work/python-rushmore/reuven-lerner/py-workout-lerner/exercise-21/*.txt"):

        out_dict[file] = longest_word(file)
    
    return out_dict


print(longest_words())
