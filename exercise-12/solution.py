from collections import Counter

# RECOMMENDED TO USE REUVEN'S SOLUTION - THIS MIGHT BE FAULTY

def most_repeating_word(input_seq: list|tuple) -> str:

    # creating a list to store the number of times the most frequen

    letter_repeat_cts: list = [sorted(Counter(item).most_common(1))[0][1]for item in input_seq]

    return input_seq[letter_repeat_cts.index(max(letter_repeat_cts))]

if __name__ == "__main__":

    words = ['this', 'is', 'an', 'elementary', 'test', 'example']

    print(most_repeating_word(words))
