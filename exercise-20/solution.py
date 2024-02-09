# Solution to main problem from exercise 20

def implement_wc(in_txt_file: str) -> dict:

    """Function that computes the number of lines, characters, words and unique
    words in a text file."""

    out_dict: dict = dict.fromkeys(("lines", "characters", "words", "unique words"), 0)                    # going to parse the file into a dictionary

    unique_words: set = set()

    with open(in_txt_file, "r", encoding = "utf-8") as f:

        for line in f:

            out_dict["lines"] += 1

            out_dict["characters"] += len(line)

            out_dict["words"] += len(line.split())

            unique_words.update(line.split())
        
    out_dict["unique words"] += len(unique_words)

    return out_dict 


out_info = implement_wc("./sample.txt")

for key, val in out_info.items():

    print(f"The number of {key} in the file is equal to {val}")
