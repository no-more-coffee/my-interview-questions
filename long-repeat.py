def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    last_char = ''
    count = 0
    maximum = 0
    for c in line:
        if c != last_char:
            maximum = max(count+1, maximum)
            count = 0
        else:
            count += 1
        last_char = c
    max1 = max(count+1, maximum)
    print(max1)
    return max1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
