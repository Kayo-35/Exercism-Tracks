def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Raising an error if non positive values are provided
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    number_factors = [
        factor
        for factor in range(1, number)
        if number % factor == 0 and factor != number
        # Excluding the number itself as indicated
    ]
    sum_of_factors = sum(number_factors)

    if number == sum_of_factors:
        return "perfect"

    return "abundant" if number < sum_of_factors else "deficient"
