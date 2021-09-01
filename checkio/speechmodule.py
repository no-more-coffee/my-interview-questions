FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def do_first(number):
    yield FIRST_TEN[number - 1]


def do_others(number):
    yield OTHER_TENS[number - 2]


def do_second(number):
    yield SECOND_TEN[number - 10]


def do_all(number):
    floor, remainder = divmod(number, 100)
    if floor:
        yield from do_first(floor)
        yield HUNDRED

    if remainder > 19:
        floor, remainder = divmod(remainder, 10)
        yield from do_others(floor)
    elif remainder > 9:
        yield from do_second(remainder)
        return

    if remainder:
        yield from do_first(remainder)


def checkio(number):
    return ' '.join(do_all(number))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
