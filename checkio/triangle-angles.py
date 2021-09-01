from math import acos, degrees


def checkio(a, b, c):
    try:
        aa = round(degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))))
        ab = round(degrees(acos((c ** 2 + a ** 2 - b ** 2) / (2 * a * c))))
    except ValueError:
        return [0, 0, 0]
    if not aa or not ab:
        return [0, 0, 0]
    ac = 180 - aa - ab
    return sorted((aa, ab, ac))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(5, 4, 3) == [37, 53, 90]
    assert checkio(10, 20, 30) == [0, 0, 0]
