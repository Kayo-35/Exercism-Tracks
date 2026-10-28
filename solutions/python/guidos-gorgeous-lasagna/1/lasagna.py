"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(time_in_oven):
    """Calculate the bake time remaining.
    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time_in_oven


def preparation_time_in_minutes(number_of_layers):
    """Calculate the total amount of time(mins) to layer the lasagna
    Parameters:
        number_of_layers(int): The amount of layers.
    Returns:
        int: The total amount of time necessary
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total amount of time spent on the lasagna preparation
    Parameters:
        number_of_layers(int): The amount of layers
        elapsed_time_in_minutes(int): The amount of time spent in the oven
    Returns
        int: The total amount of time spent in the recipe's preparation
            Calculated by the sum of both the time spent layering and in the oven
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
