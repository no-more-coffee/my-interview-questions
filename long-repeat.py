from itertools import groupby


def long_repeat(line):
    return max(len(list(v)) for k, v in groupby(line)) if line else 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat("") == 0, "Zero"
    print('"Run" is good. How is "Check"?')
