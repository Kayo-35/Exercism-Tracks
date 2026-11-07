def value(colors: list[str]) -> int | None:
    """Returns the resistance value of resistors.
    Parameters:
        colors(list[str]): The list of colors the resistor have.
    Returns:
        (int): The resistance value
    """

    colors = [color.lower() for color in colors]
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

    # If the colors provided are not present on the official list abort
    if not set(colors[:1]).issubset(set(resistor_colors)):
        return None

    return int(
        str(resistor_colors.index(colors[0])) + str(resistor_colors.index(colors[1]))
    )
