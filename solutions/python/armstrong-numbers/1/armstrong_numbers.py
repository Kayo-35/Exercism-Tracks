def is_armstrong_number(number):
    """Indicates if an int number is an armstrong number
    Parameters:
        number(int): The target number
    Returns:
        is_armstrong(boolean): Either true or false :)
    """
    # abs is essential when dealing with negative numbers
    # Otherwise - would get in the way
    amount_of_digits = len(str(abs(number)))

    amount = 0
    original_number = number
    for i in range(amount_of_digits):
        # getting from left to right
        # 153 / 10 = 15 with 3 as remainder in this example
        target_digit = int(number % 10)

        # This line is essential to discard the digit already used.
        number = int(number / 10)

        amount += target_digit**amount_of_digits

    # Evaluating
    return True if amount == original_number else False
