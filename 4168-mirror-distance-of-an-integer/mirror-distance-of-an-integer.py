class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = str(n)
        s = s[::-1]
        print(int(s))
        return abs(n - int(s))