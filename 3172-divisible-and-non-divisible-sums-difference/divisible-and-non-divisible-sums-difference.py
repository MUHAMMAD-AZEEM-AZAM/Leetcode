class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        k = n // m
        sum_multiple = m * (k * (k + 1) // 2)
        return total - 2 * sum_multiple