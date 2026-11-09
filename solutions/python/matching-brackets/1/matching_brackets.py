"""Indicates whether a string has properly enclosed ({[ chars."""


def is_paired(input_string: str) -> bool:
    """Checks if the special enclosing chars are in correct order.
    Parameters:
        input_string(str): The string to be analysed.
    Returns:
        (bool): Whether apropriate nesting is in place.
    """
    opening_chars = ("(", "[", "{")
    closing_chars = (")", "]", "}")

    # This dictionary pairs which chars must enclose which
    # Aka ( must be enclosed by ), etc
    char_pairs = dict(zip(closing_chars, opening_chars))

    # This list includes the queue for enclosing
    waiting_stack = []
    # No unnecessary whitespaces to more easily assertions
    input_string = input_string.replace(" ", "")

    # Checking each char on given string
    for char in input_string:
        # If an opening char, include it in the stack.
        if char in opening_chars:
            waiting_stack.append(char)
            # Awaiting closing...
        if char in closing_chars:
            # Now checking if the closing char is correct
            # If There is not an opening char waiting in the stack
            # Or the last in the line is not the pair of the current closing...
            # The pairing is incorrect, abort
            if len(waiting_stack) <= 0 or waiting_stack[-1] != char_pairs.get(char):
                return False
            else:
                # The stack gets smaller
                del waiting_stack[-1]

    # If all checks are a go:
    return len(waiting_stack) == 0
