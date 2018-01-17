def repeat_inside(line):
    """
        first the longest repeating substring
        Find a repeating sequence inside the substring.
        I have an example for you: in a string "abababc" - "ab" is a sequence that repeats more than once,
        so the answer will be "ababab"
    """
    # your code here
    return line

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')
