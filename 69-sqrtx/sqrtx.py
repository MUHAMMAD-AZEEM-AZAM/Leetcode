class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        low, high = 1, x
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid*mid is within bounds
            if mid * mid <= x:
                ans = mid      # mid is a candidate
                low = mid + 1  # try to find a larger one
            else:
                high = mid - 1 # mid is too large
                
        return ans