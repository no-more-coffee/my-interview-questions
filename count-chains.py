from typing import List, Tuple


def has_intersection(c1, c2):
    x1, y1, rad1 = c1
    x2, y2, rad2 = c2
    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return (rad1 + rad2) ** 2 > distance > (rad1 - rad2) ** 2


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    groups = []
    for i, c1 in enumerate(circles):
        group1 = {c1}
        for c2 in circles[i + 1:]:
            if has_intersection(c1, c2):
                group1.add(c2)
        groups.append(group1)

    result = []
    for g1 in groups:
        new_result = []
        for g2 in result:
            if g1 & g2:
                g1 |= g2
            else:
                new_result.append(g2)
        new_result.append(g1)
        result = new_result
    print(groups, result)
    return len(result)


if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
