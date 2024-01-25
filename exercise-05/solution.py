def pig_latin (english_str: str) -> str:

    if english_str[0] in 'aeiou':

        return f"{english_str}way"
    
    return f"{english_str[1:]}{english_str[0]}ay"


print(pig_latin("computer"))
print(pig_latin("python"))
print(pig_latin("air"))
