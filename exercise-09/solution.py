def firstlast(in_sequence):

    return in_sequence[:1] + in_sequence[-1:]


if __name__ == "__main__":

    print(firstlast([1,2,3,4]) == [1,4])    # testing against a list
    print(firstlast("abc") == "ac")         # testing against a string
