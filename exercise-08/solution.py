def strsort(input_string: str) -> str:
    """Sort a given string in the order of increasing Unicode value"""

    return ''.join(sorted(input_string))


if __name__ == "__main__":

    in_str: str = "cba"

    print(strsort(in_str) == "abc")
