"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """
    # Valid in this use case with O(m) performance.
    # Instead of concatenating(+) or unpacking([*rounds_1, *rounds_2])
    # Which would get O(m+n)
    rounds_1.extend(rounds_2)
    return rounds_1


def list_contains_round(rounds: list[int], number: int):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    return number in rounds


def card_average(hand: list[int]):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """
    # Using variables for readabilty
    average_on_hand = card_average(hand)
    average_first_last = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]

    return average_first_last == average_on_hand or middle_card == average_on_hand


def average_even_is_average_odd(hand: list[int]):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """
    odd_values = hand[1::2]
    even_values = hand[0::2]

    return sum(odd_values) / len(odd_values) == sum(even_values) / len(even_values)


def maybe_double_last(hand: list[int]):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] *= 2

    return hand


print(approx_average_is_average([0, 1, 5]))
