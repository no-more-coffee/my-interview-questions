# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # if not isBadVersion(n):
        #     return 0
        if isBadVersion(1):
            return 1

        first_bad = n
        last_good = 1

        while first_bad - last_good > 1:
            mid = (first_bad + last_good) // 2
            if isBadVersion(mid):
                first_bad = mid
            else:
                last_good = mid

        return first_bad
