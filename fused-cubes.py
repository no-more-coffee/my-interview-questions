from typing import Tuple, List, Iterable


def intersection(x1, x2, l1, l2) -> int:
    return min(x1 + l1, x2 + l2) - max(x1, x2)


def get_intersections(c1: Tuple[int, int, int, int], c2: Tuple[int, int, int, int]):
    return [intersection(c1[i], c2[i], c1[3], c2[3]) for i in range(3)]


def has_intersects(intersections):
    return len(tuple(a for a in intersections if a < 0)) == 0 and len(tuple(a for a in intersections if a == 0)) <= 1


def get_dots(cube: Tuple[int, int, int, int]):
    x, y, z, l = cube
    for x1 in range(x, x + l):
        for y1 in range(y, y + l):
            for z1 in range(z, z + l):
                yield x1, y1, z1


def fused_cubes(cubes: List[Tuple[int, int, int, int]]) -> Iterable[int]:
    groups = []
    for c in cubes:
        new_group = {tuple(c)}
        new_groups = [new_group]
        for g in groups:
            if any(has_intersects(get_intersections(c, c1)) for c1 in g):
                new_group |= g
            else:
                new_groups.append(g)
        groups = new_groups

    for g in groups:
        yield get_area(g)


def get_group_dots(group):
    for c in group:
        yield from get_dots(c)


def get_area(group):
    return len(set(get_group_dots(group)))


def assert1(r, r1, message):
    lasdf = sorted(fused_cubes(r))
    assert lasdf == r1, f'{message} {lasdf}!={r1}'


if __name__ == '__main__':
    assert1([(0, 0, 0, 3), (1, 2, 2, 3)], [52], 'fused')
    assert1([(0, 0, 0, 3), (1, 3, 2, 3)], [54], 'touch with faces')
    assert1([(0, 0, 0, 3), (1, 3, 3, 3)], [27, 27], 'touch with edges')
    assert1([(0, 0, 0, 3), (3, 3, 3, 3)], [27, 27], 'touch with vertices')
    assert1([(0, 0, 0, 3), (3, 4, 3, 3)], [27, 27], 'separated')
    assert1([(0, 0, 0, 3), (-2, -2, -2, 3)], [53], 'negative coordinates')
    assert1(
        [[-1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, -1, 0, 1], [0, 0, 1, 1], [0, 0, -1, 1]],
        [1, 1, 1, 1, 1, 1],
        'many')
    assert1(
        [[0, 0, -10, 1], [0, 0, -9, 1], [0, 0, -8, 1], [0, 0, -7, 1], [0, 0, -6, 1], [3, 0, -10, 1], [3, 0, -9, 1],
         [3, 0, -8, 1], [3, 0, -7, 1], [3, 0, -6, 1], [1, 4, -6, 2], [0, 0, -5, 2], [2, 0, -5, 2], [0, 1, -5, 2],
         [2, 1, -5, 2], [1, 3, -5, 2], [2, 0, -3, 2], [1, 2, -3, 2], [1, 1, -1, 2], [1, 0, 0, 2], [1, 0, 2, 2],
         [3, 0, 1, 1], [3, 0, 2, 1], [3, 0, 3, 1], [-9, 2, 6, 1], [-10, 0, 5, 2], [-9, 0, 5, 2], [-9, 0, 6, 2],
         [-11, 0, 4, 1], [-10, 0, 4, 1], [-9, 0, 4, 1], [-8, 0, 4, 1], [-7, 0, 4, 1], [-7, 0, 5, 1], [-7, 0, 6, 1],
         [-7, 0, 7, 1], [-7, 0, 8, 1], [-8, 0, 8, 1], [-11, 0, 5, 1]],
        [28, 89],
        '')

    print("Coding complete? Click 'Check' to earn cool rewards!")
