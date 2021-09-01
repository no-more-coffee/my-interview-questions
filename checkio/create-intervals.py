def create_intervals(data: set):
    """
        Create a list of intervals out of set of ints.
    """
    result = []
    current = None
    for i in sorted(data):
        if current and i == current[1] + 1:
            current[1] = i
            continue
        current = [i, i]
        result.append(current)

    return [tuple(x) for x in result]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
