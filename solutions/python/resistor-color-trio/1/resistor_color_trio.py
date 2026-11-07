def label(colors: list[str]) -> str | None:
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
    # Making sure data is uniform
    colors = [color.lower() for color in colors]

    # Simple validation
    if len(colors) < 3 or not set(colors).issubset(set(resistor_colors)):
        return None

    ohms_greatness = 10 ** resistor_colors.index(colors[2])
    base_ohms_value = (
        int(
            str(resistor_colors.index(colors[0]))
            + str(resistor_colors.index(colors[1]))
        )
        * ohms_greatness
    )

    # Assigning the correct measurement unit
    if base_ohms_value >= 1_000_000_000:
        base_ohms_value /= 1_000_000_000
        measurement_unit = " gigaohms"
    elif base_ohms_value >= 1_000_000:
        base_ohms_value /= 1_000_000
        measurement_unit = " megaohms"
    elif base_ohms_value >= 1000:
        base_ohms_value /= 1_000
        measurement_unit = " kiloohms"
    else:
        measurement_unit = " ohms"

    base_ohms_value = int(base_ohms_value)

    return str(base_ohms_value) + measurement_unit
