def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    line_len = len(line)
    for sub_len in range(line_len // 2, 0, -1):
        for i in range(0, line_len - 2 * sub_len + 1):
            for j in range(i + sub_len, line_len - sub_len + 1):
                if line[i: i + sub_len] == line[j: j + sub_len]:
                    return sub_len
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    assert double_substring('aa') == 1, "aa"
    print('"Run" is good. How is "Check"?')
