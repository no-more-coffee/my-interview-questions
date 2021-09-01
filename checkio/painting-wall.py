def get_painted_len(ops):
    return sum(y - x for x, y in get_painted(ops))


def get_painted(ops):
    for i in range(0, len(ops)):
        start, finish = ops[i]
        for j in range(i + 1, len(ops)):
            x, y = ops[j]
            if min(y, finish) - max(x, start) > 0:
                ops[j] = min(x, start), max(y, finish)
                break
        else:
            yield [start, finish]


def checkio(required, operations):
    operations = [[i - 1, j] for i, j in operations]
    for i in range(1, len(operations) + 1):
        if get_painted_len(operations[:i]) >= required:
            return i
    return -1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(15, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]]) == 4, 'new'

    assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
