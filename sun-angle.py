import math
from datetime import datetime


def sun_angle(time_str):
    time = datetime.strptime(time_str, "%H:%M")
    hours = (time.hour - 6) + time.minute / 60
    radians = hours / 12 * math.pi
    if radians < 0 or radians > math.pi:
        return "I don't see the sun!"
    return round(math.degrees(radians), 2)


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
