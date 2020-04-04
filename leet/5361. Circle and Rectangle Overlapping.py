from functools import lru_cache


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        @lru_cache
        def dist(c1, c2):
            return (c1 - c2) ** 2

        rad2 = radius ** 2
        return (
                ((y1 <= y_center <= y2) and (x1 <= x_center <= x2))
                or ((y1 <= y_center <= y2) and ((abs(x_center - x1) <= radius) or (abs(x_center - x2) <= radius)))
                or ((x1 <= x_center <= x2) and ((abs(y_center - y1) <= radius) or (abs(y_center - y2) <= radius)))
                or ((dist(x1, x_center) + dist(y1, y_center)) <= rad2)
                or ((dist(x1, x_center) + dist(y2, y_center)) <= rad2)
                or ((dist(x2, x_center) + dist(y1, y_center)) <= rad2)
                or ((dist(x2, x_center) + dist(y2, y_center)) <= rad2)
        )


print(Solution().checkOverlap(radius=1, x_center=0, y_center=0, x1=1, y1=-1, x2=3, y2=1))
print(Solution().checkOverlap(radius=1, x_center=0, y_center=0, x1=-1, y1=0, x2=0, y2=1))
print(Solution().checkOverlap(radius=1, x_center=1, y_center=1, x1=-3, y1=-3, x2=3, y2=3))
print(Solution().checkOverlap(radius=1, x_center=1, y_center=1, x1=1, y1=-3, x2=2, y2=-1))
print(Solution().checkOverlap(5, 8, 8, 9, 5, 12, 8))
print(Solution().checkOverlap(1206, -5597, -276, -5203, -1795, -4648, 1721))
