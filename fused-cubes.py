from typing import Tuple, List, Iterable


def intersection(x1, x2, l1, l2):
    return min(x1 + l1, x2 + l2) - max(x1, x2)


def fused_cubes(cubes: List[Tuple[int, int, int, int]]) -> Iterable[int]:
    a1 = intersection(cubes[0][0], cubes[1][0], cubes[0][3], cubes[1][3])
    a2 = intersection(cubes[0][1], cubes[1][1], cubes[0][3], cubes[1][3])
    a3 = intersection(cubes[0][2], cubes[1][2], cubes[0][3], cubes[1][3])
    if len(tuple(a for a in (a1, a2, a3) if a < 0)) or len(tuple(a for a in (a1, a2, a3) if a == 0)) > 1:
        return [cubes[1][3] ** 3, cubes[0][3] ** 3]
    return [cubes[1][3] ** 3 + cubes[0][3] ** 3 - (a1 * a2 * a3)]


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
