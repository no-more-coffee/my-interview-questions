def compare(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    order = kwargs.get("order")
    if len(args) == 1:
        args = list(args[0])

    value = args[0]
    for i in args:
        if order(key(i), key(value)):
            value = i

    return value


def min(*args, **kwargs):
    return compare(*args, order=lambda x, y: x < y, **kwargs)


def max(*args, **kwargs):
    return compare(*args, order=lambda x, y: x > y, **kwargs)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min(abs(i) for i in range(-10, 10)) == 0
    print('ok')
