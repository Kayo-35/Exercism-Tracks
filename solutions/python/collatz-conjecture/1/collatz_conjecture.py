def steps(number):
    """Calculates the amount of steps the number has to reach 1 on the collatz cojecture
    Parameters:
        number(int): The number to be evaluated
    Returns:
        steps(int): The amount of necessary steps.

    Examples:
        >>>steps(12)
        9
        >>>steps(20)
        7
    """

    # Validates if the value is indeed an integer
    if type(number) != int or number <= 0:
        raise ValueError("Only positive integers are allowed")

    # Calculate the necessary steps
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        steps += 1

    return steps
