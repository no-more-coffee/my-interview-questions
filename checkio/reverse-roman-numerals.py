converter_data = (
    ('I', 1,),
    ('IV', 4,),
    ('V', 5,),
    ('IX', 9,),
    ('X', 10,),
    ('XL', 40,),
    ('L', 50,),
    ('XC', 90,),
    ('C', 100,),
    ('CD', 400,),
    ('D', 500,),
    ('CM', 900,),
    ('M', 1000,),
)


def reverse_roman(roman_string):
    res = 0
    for k, v in reversed(converter_data):
        while roman_string.startswith(k):
            roman_string = roman_string[len(k):]
            res += v

    return res


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
