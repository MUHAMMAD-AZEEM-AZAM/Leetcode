class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0

        # compare with last element
        for i in range(n):
            if colors[i] != colors[-1]:
                ans = max(ans, n - 1 - i)

        # compare with first element
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                ans = max(ans, j)

        return ans       
            

