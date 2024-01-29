from pathlib import Path

def sort_and_print(in_str: str) -> str:

    """Given a string, break into individual words and sort alphabetically."""

    return ', '.join(sorted(in_str.split()))


def file_last_word(file_path: Path) -> tuple[str, str]:

    """ Return the longest and last words in a text file."""

    bag_o_words: list[str] = []

    with open(file_path, "r", encoding="utf-8") as f:

        for line in f:

            for word in line.split():

                bag_o_words.append(word.replace('.',''))
    
    longest: str = sorted(bag_o_words, key = str.__len__)[-1]

    last: str = sorted(bag_o_words, key = str.lower)[-1]

    return longest, last

if __name__ == "__main__":

    print(sort_and_print("Tom Dick Harry"))

    long, last = file_last_word(Path().absolute() / "sample.txt")

    print(long, last)
