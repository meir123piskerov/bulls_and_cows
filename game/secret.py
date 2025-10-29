import random


def generate_secret(length: int = 4, *, unique_digits: bool = True, allow_leading_zero: bool = False,
                    rng: random.Random | None = None) -> str:
    numbers = ""
    while len(numbers) != length:
        num = str(random.randrange(0,10))
        if num not in numbers:
            numbers += num
        else:
            continue
    return numbers
