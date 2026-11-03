def score(x, y):
    outer_radius_radius = 10
    inner_radius_radius = 5
    dead_center_radius = 1

    # This uses basic math to indicate a hit or miss
    # Starting from the inner to the outmost possibilities
    # <= guarantees the edge hits count as well
    if x**2 + y**2 <= dead_center_radius**2:
        return 10
    if x**2 + y**2 <= inner_radius_radius**2:
        return 5
    if x**2 + y**2 <= outer_radius_radius**2:
        return 1

    return 0
