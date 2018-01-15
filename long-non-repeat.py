def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    for i in range(len(line), 0, -1):
        for j in range(0, len(line) - i + 1):
            fragment = line[j: j + i]
            if len(fragment) == len(set(fragment)):
                return fragment
    return ''


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    assert non_repeat("fghfrtyfgh") == 'ghfrty', "ghfrty"
    print('"Run" is good. How is "Check"?')
