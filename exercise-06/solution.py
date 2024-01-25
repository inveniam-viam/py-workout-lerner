# Exercise 6 - Pig Latin Sentence

# don't need to account for capitalization or punctuation


def pl_sentence(english_sentence: str) -> str:

    """Convert an english sentence into pig latin."""

    pl_words: list[str] = []

    for word in english_sentence.split():

        if word[0] in 'aeiou':

            pl_words.append(f"{word}way")
        
        else:

            pl_words.append(f"{word[1:]}{word[0]}ay")
    

    return ' '.join(pl_words)


print(pl_sentence('this is a test translation'))


### ERRATA

#   My first solution to the problem looked like this:

def pl_sentence_first(english_sentence: str) -> str:

    """Convert an english sentence into pig latin."""

    pig_latin_sentence = ''

    for word in english_sentence.split():

        if word[0] in 'aeiou':

            pig_latin_sentence += f"{word}way "
        
        else:

            pig_latin_sentence += f"{word[1:]}{word[0]}ay"
    

    return pig_latin_sentence.strip()


print(pl_sentence_first('this is a test translation'))


# Thing is, this technically works.

# However, this isn't good practice

# Considering the fact that a string is an immutable data type
# the += operation being used on a string means that every time
# this operation is encountered, it is creating a new object

# If you're adding to a string many times, each time the += is
# encountered triggers the creation of a new object whose contents will
# be larger than the previous iteration

# In contrast, lists are mutable and adding to them with list.append
# is relatively inexpensive (both memory and compute wise)

