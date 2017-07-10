import string


def checkio(str_number, radix):
    result = 0
    revers = list(reversed(str_number))
    print('---')
    print(revers)

    for i, v in enumerate(revers):
        print(i, v)
        try:
            num = int(v)
        except ValueError:
            num = 10 + string.ascii_lowercase.index(v.lower())
        print(num)
        if num >= radix:
            return -1

        result += num * (radix ** i)
        print(result)
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
    assert checkio("909", 9) == -1, "they"
