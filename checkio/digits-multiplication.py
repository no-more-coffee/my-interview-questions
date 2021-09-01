def checkio(number):
    print('---')
    print(number)
    result = 1
    while number >= 10:
        remains = number % 10
        number //= 10
        print(number, remains)
        if remains:
            result *= remains
    return number * result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == 2
    assert checkio(200) == 2
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
