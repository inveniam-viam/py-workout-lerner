def redefine_mysum(*args):

    if not args:

        return args
    
    output = args[0]

    for item in args[1:]:

        output += item 
    

    return output

if __name__ == "__main__":

    print(redefine_mysum("abc", "def") == "abcdef")
    print(redefine_mysum([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])

