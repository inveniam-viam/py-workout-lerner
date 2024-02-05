# Solutions to additional problems
from collections import Counter

# Solution to 16.1


def sum_ints_from_txt(in_file: str) -> int:

    out_list: list[int] = []

    with open(in_file, "r", encoding = "utf-8") as f:

        for line in f:

            for word in line.split():

                if word.isdigit():

                    out_list.append(int(word))
    
    return sum(out_list)

# 16.2




# Solution to 16.3 (version 1 - not allowed to initialize a dictionary of vowels)

def file_vowel_counts(in_file: str) -> dict:

    vowel_dict: dict = {}

    with open(in_file, "r", encoding = "utf-8") as file:

        for line in file:

            vowel_counts = dict(Counter(letter for letter in line.lower() if letter in "aeiou"))

            for key in vowel_counts.keys():

                vowel_dict[key] = vowel_dict.get(key, 0) + vowel_counts[key]
    
    return vowel_dict

# Solution to 16.3 (version 2 - allowed to make a source dictionary for the vowels)
    

def vowels_in_file(in_file: str):

    out_dict: dict = dict.fromkeys("aeiou", 0)

    with open(in_file, "r", encoding = "utf-8") as file:

        for line in file:

            for letter in line.lower():

                if letter in out_dict:

                    out_dict[letter] += 1
    
    return out_dict

            




 