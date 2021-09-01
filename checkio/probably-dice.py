from collections import defaultdict


def probability(dice_number, sides, target):
    first_dice = tuple((x, 1 / sides) for x in range(1, sides + 1))
    result = dict(first_dice)

    for _ in range(1, dice_number):
        source = ((x + y, px * py) for x, px in result.items() for y, py in first_dice)

        result = defaultdict(int)
        for key, value in source:
            result[key] += value

    try:
        return result[target]
    except KeyError:
        return 0.0000


def almost_equal(checked, correct, significant_digits=4):
    precision = 0.1 ** significant_digits
    return correct - precision < checked < correct + precision


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    assert (almost_equal(probability(1, 2, 999), 0.0000)), "KeyError: 999, probability, 15"
    assert (almost_equal(probability(1, 6, 3), 0.1667)), "Basic example"
    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example1"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
