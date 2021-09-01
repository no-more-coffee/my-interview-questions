converter_data = (
    (1, 'I',),
    (4, 'IV'),
    (5, 'V',),
    (9, 'IX'),
    (10, 'X',),
    (40, 'XL'),
    (50, 'L',),
    (90, 'XC'),
    (100, 'C',),
    (400, 'CD'),
    (500, 'D',),
    (900, 'CM'),
    (1000, 'M',),
)


def checkio(data):
    result = ''
    for k, v in reversed(converter_data):
        floor, data = divmod(data, k)
        result += floor * v

    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    assert checkio(1954) == 'MCMLIV', '1954'
    assert checkio(1990) == 'MCMXC', '1990'
    assert checkio(2014) == 'MMXIV', '2014'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(6) == 'VI', '6'
