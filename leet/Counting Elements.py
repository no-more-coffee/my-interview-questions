from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        incr_arr = tuple(i + 1 for i in sorted_arr)
        i = 0
        j = 1
        c = 0
        while i < len(arr) and j < len(arr):
            if incr_arr[i] == sorted_arr[j]:
                c += 1
                i += 1
            elif incr_arr[i] > sorted_arr[j]:
                j += 1
            else:
                i += 1

        return c


print(Solution().countElements([1, 2, 3]), 2)
print(Solution().countElements([1, 1, 3, 3, 5, 5, 7, 7]), 0)
print(Solution().countElements([1, 3, 2, 3, 5, 0]), 3)
print(Solution().countElements([1, 1, 2, 2]), 2)
print(Solution().countElements([1, 1, 2]), 2)
