# A global variable, in a better way this would be a property of a given
# class which its methods could manipulate, in order to reduce either copy
# and past or redundant parameters in functions
resistor_colors = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def color_code(color: str) -> int | None:
    """Returns the code a given color represents in resistors.
    Parameters:
        color(str): The resistor's color.
    Returns:
        (int): The associated value
    """
    if color.lower() in resistor_colors:
        return resistor_colors.index(color)

    return None


def colors() -> list[str]:
    """Returns the list of available resistor colors."""
    return resistor_colors
