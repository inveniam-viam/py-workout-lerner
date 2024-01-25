# Exercise 2 - Additional Problems

# 1 - add starting point to the sum function

def my_sum_more(start: int = 0, *collection) -> int:

    final_sum = start

    for item in collection:

        final_sum += item
    
    return final_sum

#2 - Function that averages numbers

def calculate_average(numbers: list[int]):

    list_sum = my_sum_more(*numbers)

    return list_sum / len(numbers)


#3 - Function that plays with word lengths

def word_lengths(*collection):

    """Function that takes a list of words and returns a tuple containing three integers
        representing the length of the shortest word, the length of the longest word and the average word length"""
    sigma = 0

    smallest: int = len(collection[0])
    largest: int = len(collection[0])


    for word in collection:

        if len(word) >= largest:

            largest = len(word)
        
        elif len(word) < smallest:

            smallest = len(word)
        
        sigma += len(word) 
    
    return (smallest, largest, sigma/len(collection))


def object_sums(*collection):

    """Function that returns the sum of objects that are either integers or can be turned into integers."""

    final_sum = 0

    for item in collection:

        if check := int(item):

            final_sum += check

    return final_sum





if __name__ == "__main__":

    print(my_sum_more(4, 1, 2, 3, 4, 5, 6))
    print(my_sum_more(4, *[1, 2, 3, 4, 5, 6]))


    print(calculate_average([1, 2, 3, 4, 5]))

    print(word_lengths("he", "she", "i"))

    print(object_sums(1, 2, 3, "5"))
