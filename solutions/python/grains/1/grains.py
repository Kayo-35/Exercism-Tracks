def square(number):
    """Calculates the amount of grain on a given square
    Parameters:
        number(int): The target square
    Returns:
        amount(int): The amount of grains
    Examples:
    >>>square(8)
    128
    """
    # Validates if the given square exists
    if not isinstance(number, int) or number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")

    # Since the first square has a single grain it starts with 2⁰
    # So to each square the power is elevated to the square number - 1
    return 2 ** (number - 1)


def total():
    """Calculates the total amount of grains on the entire square
    Returns:
        amount(int): The total amount of grains in the square
    """

    # To calculate the total amount it is necessary to get the sum
    # of all the grains in each square.
    amount = 0
    for square in range(64):
        amount += 2**square

    return amount
