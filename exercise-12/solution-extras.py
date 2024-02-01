# Additional Exercises from Week 12

from collections import Counter

# a more pythonic, readable solution to 12.1

def repeating_vowel_count(word: str) -> int:
    """For a given word, this function returns the number of times the vowel that repeats the most appears, in a given word"""
    return Counter(letter for letter in word if letter in "aeiou").most_common(1)[0][1]

def max_repeating_vowels(words: list[str]) -> str:
    """Returns the word in a given list that has the highest instance of a repeating vowel"""
    return max(words, key = repeating_vowel_count)


print(max_repeating_vowels(["helly", "world", "kyeps", "peeling"]))


# 12.2 and 12.3 not posted since it contains personal information
