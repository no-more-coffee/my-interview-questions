from datetime import datetime


def time_converter(time_str):
    time = datetime.strptime(time_str, '%H:%M')
    converted = f'{time:%I:%M %p}'
    formatted = converted.lstrip("0").lower().replace('m', '.m.')
    return formatted


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
