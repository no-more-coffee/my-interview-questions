class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        fives = 5
        threes = 3
        for i in range(1, n + 1):
            fives -= 1
            threes -= 1
            if not fives and not threes:
                res.append('FizzBuzz')
                fives = 5
                threes = 3
            elif not threes:
                res.append('Fizz')
                threes = 3
            elif not fives:
                res.append('Buzz')
                fives = 5
            else:
                res.append(str(i))

        return res
