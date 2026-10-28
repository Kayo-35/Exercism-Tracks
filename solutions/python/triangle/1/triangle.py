def equilateral(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] and sides[1] == sides[2]
    return False


def isosceles(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] or sides[0] == sides[2] or sides[2] == sides[1]
    return False


def scalene(sides):
    if is_triangle(sides):
        return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
    return False


def is_triangle(sides):
    return (
        all(side > 0 for side in sides)
        and sides[0] + sides[1] >= sides[2]
        and sides[1] + sides[2] >= sides[0]
        and sides[0] + sides[2] >= sides[1]
    )
