class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        if numRows == 0:
            return res

        if numRows >= 1:
            res.append([1])

        if numRows >= 2:
            res.append([1, 1])

        if numRows == 2:
            return res

        last = [1, 1]
        for i in range(2, numRows):
            r = [1]
            for j in range(1, len(last)):
                r.append(last[j - 1] + last[j])
            r.append(1)
            last = r
            res.append(r)
        return res
