class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s , m = 0, 1
        for c in str(n):
            s += int(c)
            m *= int(c)

        return m - s

