import re


def is_valid(isbn: str):
    isbn = isbn.replace("-", "")

    # Checking for the correct pattern
    if not re.match(r"^[0-9]{9}[0-9X]$", isbn):
        return False

    # Calculating
    final_product = 0
    for index, factor in enumerate(range(10, 0, -1)):
        if isbn[index] == "X":
            final_product += 10 * factor
        else:
            final_product += int(isbn[index]) * factor

    return final_product % 11 == 0
