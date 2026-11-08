"""Module to calculate and display resistance and tolerance values for electrical resistors."""

resistor_colors = (
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
)
tolerance_colors = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def resistor_label(colors: list[str]) -> str:
    """Calculates and present the resistance/tolerance values of resistors.
    Parameters:
        colors(list[str]): The colors the resistor is made of.
    Returns:
        (str): The given resistance and tolerance values
    """

    # If it is a only band black registor:
    if len(colors) == 1 and colors[0].lower() == "black":
        return "0 ohms"

    # Validation
    if not validate_colors(colors):
        raise ValueError("The colors provided are invalid!")

    # Calculating the resistance
    resistance_in_ohms = calculate_ohms(colors[:-1])

    # Formatting the value for display
    formatted_ohms = formatting_ohms(resistance_in_ohms)

    # Get the tolerance
    tolerance = tolerance_colors[colors[-1]]

    # Returning the entire data
    return formatted_ohms + " ±" + str(tolerance) + "%"


def validate_colors(colors: list[str]) -> bool:
    """Validates the colors provided for resistors.
    Parameters:
        colors(list[str]): The colors the resistor is made of.
    Returns:
        (bool): Whether or not the colors are valid.
    """
    # Minimum amount of colors
    if len(colors) not in [4, 5]:
        return False

    # Correct colors
    if (
        not set(colors[:-1]).issubset(resistor_colors)
        or colors[-1] not in tolerance_colors
    ):
        return False

    return True


def calculate_ohms(colors: list[str]) -> int:
    """Calculate the amount of ohms the resistor has per its colors.
    Parameters:
        colors(list[str]): The colors that represent the resistance value.
    Returns:
        (int): The total resistance.
    """

    if len(colors) == 3:
        base_number = int(
            str(resistor_colors.index(colors[0]))
            + str(resistor_colors.index(colors[1]))
        )
        resistance_in_ohms = base_number * 10 ** resistor_colors.index(colors[2])
    else:
        resistance_in_ohms = int(
            str(resistor_colors.index(colors[0]))
            + str(resistor_colors.index(colors[1]))
            + str(resistor_colors.index(colors[2]))
        ) * 10 ** resistor_colors.index(colors[3])

    return resistance_in_ohms


def formatting_ohms(total_ohms: int) -> str:
    """Formats the amount of given ohms to its more adequate measurement unit.
    Parameters:
        total_ohms(int): The amount of ohms
    Returns:
        (str): The formatted string of how the value would be said out loud.
    Examples:
        >>> formatting_ohms(1230)
        >>> "1.23 kilooms"
    """

    gigaohm = 1_000_000_000
    megaohm = 1_000_000
    kiloohm = 1000

    if total_ohms >= gigaohm:
        # The ternary operator allows the singular case where:
        # total_ohms is multiple of a given grouping, so the value should be int not a float
        total_ohms = (
            total_ohms / gigaohm if total_ohms % gigaohm != 0 else total_ohms // gigaohm
        )
        return str(total_ohms) + " gigaohms"
    if total_ohms >= megaohm:
        total_ohms = (
            total_ohms / megaohm if total_ohms % megaohm != 0 else total_ohms // megaohm
        )
        return str(total_ohms) + " megaohms"
    if total_ohms >= kiloohm:
        total_ohms = (
            total_ohms / kiloohm if total_ohms % kiloohm != 0 else total_ohms // kiloohm
        )
        print(total_ohms % kiloohm != 0)
        return f"{total_ohms:g} kiloohms"

    return str(total_ohms) + " ohms"
