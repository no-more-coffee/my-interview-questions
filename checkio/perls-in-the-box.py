from collections import Counter


def checkio(marbles: str, step: int) -> float:
    marbles_d = {'b': 0, 'w': 0, **dict(Counter(marbles).items())}
    LEN = len(marbles)

    def do(balls, probability, step):
        if step == 1:
            w_probability = balls['w'] / LEN
            return w_probability * probability

        if balls['w']:
            w_probability = balls['w'] / LEN
            probability_probability = w_probability * probability
            sum2 = do({'b': balls['b'] + 1, 'w': balls['w'] - 1}, probability_probability, step - 1)
        else:
            sum2 = 0

        if balls['b']:
            b_probability = balls['b'] / LEN
            f = b_probability * probability
            sum1 = do({'b': balls['b'] - 1, 'w': balls['w'] + 1}, f, step - 1)
        else:
            sum1 = 0

        return sum1 + sum2
    return round(do(marbles_d, 1, step), 2)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio('bbw', 3))

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
