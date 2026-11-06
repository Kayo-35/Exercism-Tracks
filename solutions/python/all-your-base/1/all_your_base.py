def rebase(input_base: int, digits: list[int], output_base: int):
    # Including a standalone function to this crucial step
    validate(input_base, digits, output_base)

    # To convert a value to base x from base y;
    # If base neither base x or y is decimal:
    #   x must be converted to the decimal base
    #   Then converted to the desired base

    base_ten_form = (
        convert_to_base_ten(digits, input_base)
        if input_base != 10
        # Converting the digits to a number if already valid
        else int("".join([str(digit) for digit in digits]))
    )

    if output_base == 10:
        return [int(digit) for digit in str(base_ten_form)]

    return convert_from_base_ten_to_any_base(base_ten_form, output_base)


def convert_to_base_ten(number_digits: list[int], input_base: int):
    # Conversion method: Multiplying the digits, right to left, adding the next digit,
    # them saving the result and repeating until digits are exausted

    # Edge case: Single digit value or empty lists provided as digits
    if not number_digits or len(number_digits) == 1:
        return number_digits[0] * input_base**0 if number_digits else 0

    # Initializing the auxiliary varible
    value_conversion = number_digits[0] * input_base + number_digits[1]

    # Excluding the last digit
    for i in range(1, len(number_digits) - 1):
        value_conversion = value_conversion * input_base + number_digits[i + 1]

    return value_conversion


def convert_from_base_ten_to_any_base(number: int, desired_base: int):
    # Initializing the variables that conditionally control
    # The logical flow
    quocient = number // desired_base
    remainders = [number % desired_base]

    while quocient >= desired_base:
        remainders.append(quocient % desired_base)
        # Trucantes the value, We only want INTs!
        quocient //= desired_base

    # Complicated way to say take the last quocient and concatenate with
    # the digits found in the remainders
    remainders.reverse()  # The values must be reversed when building the number
    final_number_digits = [quocient]
    final_number_digits.extend([digit for digit in remainders])

    # Removing leading zeros if nedeed
    if final_number_digits[0] == 0:
        del final_number_digits[0]
    return final_number_digits


def validate(input_base: int, digits: list[int], output_base: int):
    # If input base is lesser than two:
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # A safeguard against funny business :)
    if any(not number.is_integer() for number in [input_base, *digits, output_base]):
        raise ValueError("The arguments must be integer values!")

    # If any of the digits in the input is greater than the input_base
    if any(digit >= input_base or digit < 0 for digit in (digits)):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # If output_base is lesser than two...
    if output_base < 2:
        raise ValueError("output base must be >= 2")


print(rebase(2, [], 10))
