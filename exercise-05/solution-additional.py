# Re-implementing the pig latin function

# handle capitalization
# handle punctuation
# pig latin - alternative version


def better_pig_latin(english_str: str) -> str:

    """Converts an English word to the Pig Latin form"""

    english_string = english_str.lower()

    if english_string[0] in 'aeiou':

        if english_string[-1] in '!.:;':

            pig_latin_version = f"{english_string:-1}way{english_string[-1]}"
        
        else:

            pig_latin_version = f"{english_string}way"

    else:
        if english_string[-1] in '!.:;':

            pig_latin_version = f"{english_string[1:-1]}{english_string[0]}ay{english_string[-1]}"
        else:
            pig_latin_version = f"{english_string[1:]}{english_string[0]}ay"
 
    # check for capitalization

    if english_str[0].isupper():

        return pig_latin_version.title()
    
    return pig_latin_version


print(better_pig_latin("Python!"))
