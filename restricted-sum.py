def fun(x, *other):
    return x + fun(*other) if other else x


def checkio(data):
    return fun(*data)


if __name__ == '__main__':
    assert checkio([1, 2, 3]) == 6
    assert checkio([2, 2, 2, 2, 2, 2]) == 12
