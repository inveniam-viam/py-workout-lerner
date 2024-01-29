def even_odd_sums(nums: tuple|list) -> list:

    return [sum(nums[::2]), sum(nums[1::2])]

def plus_minus(nums: list|tuple) -> float:

    sum_elements: float = nums[0]

    for i in range(1, len(nums)):

        if i % 2 == 0:

            sum_elements += (-1 * nums[i])
        else:
            sum_elements += nums[i]

    return sum_elements
        




print(even_odd_sums([10, 20, 30, 40, 50, 60]))
print(plus_minus([10, 20, 30, 40, 50, 60]))
print(plus_minus((10, 20, 30, 40, 50, 60)))
