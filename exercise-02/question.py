# Exercise 2

def mysum(*numbers):

    """Implementing a version of the in-built sum function for a sequence."""

    final_sum = 0

    for number in numbers:

        final_sum += number
        
    return final_sum 


if __name__ == "__main__":

    print(mysum(1, 2, 3, 4, 5, 6))
    print(mysum(*[1, 2, 3, 4, 5, 6]))
