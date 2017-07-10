def is_even(x):
    return (x % 2) != 0


def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    print("---")
    print(array)
    if not array:
        return 0

    even_sum = sum(v for k, v in enumerate(array) if k % 2 == 0)
    return even_sum * array[-1]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([]) == 0, "An empty array = 0"
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
