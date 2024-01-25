from pathlib import Path

file_path = Path().absolute() / "exercise-06"

def nonsense_maker(file: Path) -> str:

    """A function that takes a text file and
    creates a nonsensical sentence from the nth word on
    each line where n is the line number."""

    sentence_words: list[str] = []

    with open(file, "r", encoding = "utf-8") as f:

        for line_num, line in enumerate(f):

            sentence_words.append(line.split()[line_num])
  
    return ' '.join(sentence_words)




print(nonsense_maker(file_path / "sample-text.txt"))
