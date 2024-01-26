def ubbi_dubbi(english_str: str) -> str:
    """Convert an english word to its 'ubbi-dubbi' equivalent"""
    out_list: list[str] = []

    for letter in english_str:

        if letter in "aeiou":

            out_list.append(f"ub{letter}")
        else:
            out_list.append(letter)
    return ''.join(out_list)

if __name__ == "__main__":

    octopus: str = ubbi_dubbi("octopus")
    elephant: str = ubbi_dubbi("elephant")
    soap: str = ubbi_dubbi("soap")

    # unit tests
    print(octopus == "uboctubopubus")
    print(elephant == "ubelubephubant")
    print(soap == "suboubap")
