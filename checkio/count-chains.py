from typing import List, Tuple


def has_intersection(c1: tuple, c2: tuple) -> bool:
    x1, y1, rad1 = c1
    x2, y2, rad2 = c2
    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return (rad1 + rad2) ** 2 > distance > (rad1 - rad2) ** 2


def has_group_intersection(c1: tuple, group: set) -> bool:
    for c2 in group:
        if has_intersection(c1, c2):
            return True
    return False


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    groups = []
    for c in circles:
        new_group = {c}
        new_groups = [new_group]
        for group in groups:
            if has_group_intersection(c, group):
                new_group |= group
            else:
                new_groups.append(group)
        groups = new_groups

    return len(groups)


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
