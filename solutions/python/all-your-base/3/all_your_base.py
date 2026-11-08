def rebase(input_base: int, digits: list[int], output_base: int):
    # Including a standalone function to this crucial step
    validate(input_base, digits, output_base)

    base_ten_form = sum(
        [
            digit * input_base**exponent
            for exponent, digit in enumerate(reversed(digits))
        ]
    )

    if output_base == 10:
        base_ten_form = [int(digit) for digit in str(base_ten_form)]
        return base_ten_form

    output_digits = []
    while True:
        remainder = base_ten_form % output_base
        base_ten_form //= output_base

        output_digits.append(remainder)

        if base_ten_form < output_base:
            output_digits.append(base_ten_form)
            break

    output_digits.reverse()

    # Removing trailing zeros cases
    if all(digit == 0 for digit in output_digits):
        output_digits = [0]

    return output_digits


def validate(input_base: int, digits: list[int], output_base: int):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # A safeguard against funny business :)
    if any(not number.is_integer() for number in [input_base, *digits, output_base]):
        raise ValueError("The arguments must be integer values!")

    if any(digit >= input_base or digit < 0 for digit in (digits)):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2:
        raise ValueError("output base must be >= 2")
