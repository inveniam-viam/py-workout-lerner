def even_odd_sums_original(nums: tuple|list) -> list:

    return [sum(nums[::2]), sum(nums[1::2])]

# alternative implementation

def even_odd_sums_alternate(input_sequence: list|tuple) -> list[int]:

    even_sum = sum([value
                    for index, value in enumerate(input_sequence)
                    if index %2 == 0])
    
    odd_sum = sum([value 
                   for index, value in enumerate(input_sequence)
                   if index %2 != 0])
    
    return [even_sum, odd_sum]

def plus_minus (input_sequence: list|tuple) -> int:

    total_sum: int = input_sequence[0]

    total_sum += sum([
        value if index %2 == 0 else -value 
        for index, value in enumerate(input_sequence[1:])
    ])

    return total_sum
        




print(even_odd_sums_original([10, 20, 30, 40, 50, 60]))
print(plus_minus([10, 20, 30, 40, 50, 60]))
print(plus_minus((10, 20, 30, 40, 50, 60)))
