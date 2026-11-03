def is_valid(isbn: str):
    # Standardizing the data
    isbn = isbn.replace("-", "").lower()

    # Check if the isbn is 10 digits.
    # If it has a letter it must be an x.
    if (
        not isbn[:-1].isdigit()
        or len(isbn) != 10
        or not (isbn[-1].isdigit() or isbn[-1] == "x")
    ):
        return False

    # Calculating
    final_product = 0
    for index, factor in enumerate(range(10, 0, -1)):
        if isbn[index] == "x":
            final_product += 10 * factor
        else:
            final_product += int(isbn[index]) * factor

    return final_product % 11 == 0
