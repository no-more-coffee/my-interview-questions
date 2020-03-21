from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d = {}
        for r, c in reservedSeats:
            d.setdefault(r, []).append(c)

        res = n * 2
        for r, items in d.items():
            free24, free69, free47 = True, True, True
            for col in items:
                if 2 <= col <= 5:
                    free24 = False
                if 6 <= col <= 9:
                    free69 = False
                if 4 <= col <= 7:
                    free47 = False
            if free24 and free69:
                continue
            if free24 or free69 or free47:
                res -= 1
                continue
            res -= 2
        return res


print(Solution().maxNumberOfFamilies(n=3, reservedSeats=[[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
print(Solution().maxNumberOfFamilies(n=2, reservedSeats=[[2, 1], [1, 8], [2, 6]]))
print(Solution().maxNumberOfFamilies(n=4, reservedSeats=[[4, 3], [1, 4], [4, 6], [1, 7]]))
