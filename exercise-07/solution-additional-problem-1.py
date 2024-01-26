def better_ubbi_dubbi(english_word: str) -> str:

    output_word: list[str] = []

    for letter in english_word.lower():

        if letter in "aeiou":

            output_word.append(f"ub{letter}")
        else:
            output_word.append(letter)
    
    out_word = ''.join(output_word)

    if english_word.istitle():

        return out_word.title()
    
    else:

        return out_word


if __name__ == "__main__":

    octopus: str = better_ubbi_dubbi("Octopus")
    elephant: str = better_ubbi_dubbi("elephant")
    soap: str = better_ubbi_dubbi("soap")
    
    # unit tests
    print(octopus == "Uboctubopubus")
    print(elephant == "ubelubephubant")
    print(soap == "suboubap")
