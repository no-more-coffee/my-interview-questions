from typing import List

full_lines = (
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((1, 0), (1, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (0, 1), (0, 2)),
    ((2, 0), (2, 1), (2, 2)),
)

X_FULL_LINE = tuple('XXX')
O_FULL_LINE = tuple('OOO')


def checkio(game_result: List[str]) -> str:
    for line in full_lines:
        line_elements = tuple(game_result[x][y] for x, y in line)
        if line_elements == X_FULL_LINE:
            return "X"
        if line_elements == O_FULL_LINE:
            return "O"
    return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
