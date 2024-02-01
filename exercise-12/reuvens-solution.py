# Reuven's solution of the same problem

# Differences in approach:

# I computed the highest appearing letter's count in each word
# and returned that index from the original list 

# Reuven computes the same, but he calls the max function on the original
# list with the key being the function he used to compute the 
# highest appearing letter counts

from collections import Counter

def compute_highest_repeating_letter(word: str) -> int:
    """For a word, this calculates the letter that repeats the most often"""

    return Counter(word).most_common(1)[0][1] 

def word_with_highest_repeat(words: list[str]) -> str:
    """From a list of words, this function returns the word
    that has the highest number of instances of a repeating letter"""

    return max(words, key = compute_highest_repeating_letter)


if __name__ == "__main__":

    # quick small test

    words = ['this', 'is', 'an', 'elementary', 'test', 'example']

    print(word_with_highest_repeat(words) == "elementary")
