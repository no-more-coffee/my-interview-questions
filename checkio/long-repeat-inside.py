def repeat_inside(line):
    """
        first the longest repeating substring
        Find a repeating sequence inside the substring.
        I have an example for you: in a string "abababc" - "ab" is a sequence that repeats more than once,
        so the answer will be "ababab"
    """
    line_len = len(line)
    results = ['']
    for sub_len in range(1, (line_len // 2) + 1):
        for i in range(0, line_len - 2 * sub_len + 1):
            target_str = line[i: i + sub_len]
            tries = (line_len - i) // sub_len
            matches = 0
            for j in range(1, tries):
                next_str = line[i + j * sub_len: i + (j + 1) * sub_len]
                if next_str != target_str:
                    break
                matches += 1
            if matches:
                results.append(target_str * (matches + 1))
    return max(results, key=len)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('abc') == '', "Forth"
    print('"Run" is good. How is "Check"?')
