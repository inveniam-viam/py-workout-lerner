# Solution to additional problems from exercise 24

# Problem 1

def copyfile(input_file, *args):

    with open(input_file, "r", encoding = "utf-8") as f:

        content = f.readlines()
    
    for file in args:

        with open(file, "w", encoding = "utf-8") as f2:

            for line in content:

                f2.write(line)

# Problem 2
                
def factorial(*args):

    out_product = 1

    if len(args) >= 1:

        for num in args:

            out_product *= num 
        
        return out_product
    
    return 0


# Problem 3


def anyjoin(input_sequence, glue = ' '):

    return glue.join(str(char) for char in input_sequence)
