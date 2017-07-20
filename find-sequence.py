from itertools import chain


def find_same_elements(m: iter):
    count = 1
    for row in m:
        for j in range(1, len(row)):
            if row[j] == None:
                continue
            if row[j] == row[j - 1]:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 1
    return False


def checkio(matrix):
    if find_same_elements(matrix):
        return True

    rotated = zip(*matrix)
    if find_same_elements(rotated):
        return True

    diag1 = []
    for i, row in enumerate(matrix):
        row = chain([None] * (len(row) - 1 - i), row, [None] * i)
        l = list(row)
        diag1.append(l)
    rotated = zip(*diag1)
    if find_same_elements(rotated):
        return True

    diag2 = []
    for i, row in enumerate(matrix):
        row = chain([None] * i, row, [None] * (len(row) - 1 - i))
        values = list(row)
        diag2.append(values)
    rotated = zip(*diag2)
    if find_same_elements(rotated):
        return True

    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
