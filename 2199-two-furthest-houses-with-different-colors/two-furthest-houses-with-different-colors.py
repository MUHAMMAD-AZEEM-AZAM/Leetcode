class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        j =len(colors)-1
        n = len(colors)
        i = 0
        ans = 0
        while i < len(colors)-1 or j > 0:
            if colors[i] != colors[-1]:
                ans = max(ans, n - 1 - i)
            if colors[j] != colors[0]:
                ans = max(ans, j)    
            j -= 1
            i += 1     
        return ans            
            

