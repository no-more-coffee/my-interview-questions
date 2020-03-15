from typing import Tuple, List, Iterable


def intersection(x1, x2, l1, l2) -> int:
    return min(x1 + l1, x2 + l2) - max(x1, x2)


def get_intersections(c1: Tuple[int, int, int, int], c2: Tuple[int, int, int, int]):
    return [intersection(c1[i], c2[i], c1[3], c2[3]) for i in range(3)]


def has_intersects(intersections):
    return len(tuple(a for a in intersections if a < 0)) == 0 and len(tuple(a for a in intersections if a == 0)) <= 1


def fused_cubes(cubes: List[Tuple[int, int, int, int]]) -> Iterable[int]:
    groups = []
    for c in cubes:
        new_group = {c}
        new_groups = [new_group]
        for g in groups:
            if any(has_intersects(get_intersections(c, c1)) for c1 in g):
                new_group |= g
            else:
                new_groups.append(g)
        groups = new_groups

    # if not has_intersects(get_intersections()):
    #     return [cubes[1][3] ** 3, cubes[0][3] ** 3]
    # return [cubes[1][3] ** 3 + cubes[0][3] ** 3 - (a1 * a2 * a3)]


if __name__ == '__main__':
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)])) == [52], 'fused'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)])) == [54], 'touch with faces'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)])) == [27, 27], 'touch with edges'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 3, 3, 3)])) == [27, 27], 'touch with vertices'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 4, 3, 3)])) == [27, 27], 'separated'
    assert sorted(fused_cubes([(0, 0, 0, 3), (-2, -2, -2, 3)])) == [53], 'negative coordinates'
    assert sorted(
        fused_cubes([[-1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, -1, 0, 1], [0, 0, 1, 1], [0, 0, -1, 1]])
    ) == [1, 1, 1, 1, 1, 1], 'many'
    print("Coding complete? Click 'Check' to earn cool rewards!")
