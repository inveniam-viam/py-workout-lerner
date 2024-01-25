import decimal

def funky_before_and_after(num: float, before: int, after: int) -> float:

    before_decimal: int = int(num % (10** before))

    after_decimal: int = int((num * (10 ** after)) % (10 ** after))

    return (before_decimal + (after_decimal / 10**after))


def decimals_and_strings() -> decimal.Decimal:

    num_one = input("Enter a decimal number: ")
    num_two = input("Enter another decimal number: ")

    return decimal.Decimal(num_one) + decimal.Decimal(num_two)


if __name__ == "__main__":

    print(decimals_and_strings())
