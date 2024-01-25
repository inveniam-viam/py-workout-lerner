def x_base_to_decimal(num: str, base: int) -> int:


    int_value: int = 0

    for power, digit in enumerate(reversed(num)):

        int_value += int(digit, base) * (base ** power)
    
    return int_value



if __name__ == "__main__":

    num = input("Enter a number: ")
    base = int(input("Specify the base: "))

    print(f"{num} converted to decimal is {x_base_to_decimal(num, base)}")
