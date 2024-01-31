# Solutions to Additional Problems - Exercise 11

# Problem 1
def sort_by_absolute_value(input_sequence: list|tuple) -> list:
    """Given a sequence of positive and negative numbers, this function
    sorts them by absolute value."""
    # sorted can be run on any iterable, so whether the input sequence is a 
    # list or tuple does not matter
    return sorted(input_sequence, key = abs)


# Problem 2, Implementation 1

def sort_by_vowelcount(input_list: list[str]|tuple) -> list[str]:

    """Given a list of strings, this function sorts them by how many vowels they contain."""
    # calling the sorted function on the iterable with the key being a helper function's result
    return sorted(input_list, key = vowel_count)

def vowel_count(word):

    """Helper function to assist in vowel count"""

    total_vowels: int = 0

    for char in word:

        if char in "aeiou":

            total_vowels += 1
    
    return total_vowels

# Problem 2, Implementation 2

def vowel_sort_alt(input_seq: list|tuple) -> list:

    vowel_counts = [sum(1 if char.lower() in "aeiou" else 0 for char in word) for word in input_seq]

    zipped_counts = list(zip(input_seq, vowel_counts))

    sorted_counts = sorted(zipped_counts, key = lambda x: (x[1], x[0]))

    return [item[0] for item in sorted_counts]

def vowelsort_oneliner(input_seq: list|tuple) -> list:

    return sorted(input_seq, key = lambda x: sum(1 if char.lower() in "aeiou" else 0 for char in x))

# Problem 3

def listsort_by_sum(input_seq: list) -> list:
    """Given a list of lists, with each function containing zero or more
    number, this function sorts the list by the sum of each inner lists' numbers."""
    return sorted(input_seq, key = sum)


if __name__ == "__main__":

    # Additional Problem 1

    unsorted_inseq = [-20, -5, 10, 15, -30, 3]

    sorted_inseq = sort_by_absolute_value(unsorted_inseq)

    # test-case

    expected_sort = [3, -5, 10, 15, -20, -30]

    print(sorted_inseq == expected_sort)


    # Additional Problem 2

    unsorted_fruits = ["apple", "pear", "banana", "grape"]
    unsorted_python = ["hello", "world", "python", "programming"]
    unsorted_sky = ("sky", "blue", "green", "yellow")


    print(sort_by_vowelcount(unsorted_fruits))
    print(sort_by_vowelcount(unsorted_python))
    print(sort_by_vowelcount(unsorted_sky))

    print(vowel_sort_alt(unsorted_fruits))

    print(vowelsort_oneliner(unsorted_sky))








