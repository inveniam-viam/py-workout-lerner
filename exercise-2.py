# Exercise 2 - Summing Numbers


def mysum(*numbers) -> int:

    my_sum: int = 0

    for number in numbers:

        my_sum += number 
    

    return my_sum

print(mysum(1, 2, 3))

print(mysum(1, 2, 3, 4))

print(mysum(*[1, 2, 3, 4, 5, 6]))


def built_sum(start, *numbers):

    out = start 

    for number in numbers:

        out += number 
    
    return out 

print(built_sum(4, *[1,2,3,4]))
