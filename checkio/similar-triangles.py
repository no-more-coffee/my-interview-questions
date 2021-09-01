from typing import List, Tuple

Coords = List[Tuple[int, int]]


def get_side_square(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def get_side_squares(coords):
    return sorted(
        get_side_square(*coords[i - 1], *coords[i])
        for i
        in range(len(coords))
    )


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    pa, pb, pc = (l1 / l2 for l1, l2 in zip(get_side_squares(coords_1), get_side_squares(coords_2)))
    return pa == pb == pc


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
