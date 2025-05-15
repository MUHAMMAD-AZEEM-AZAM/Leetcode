class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        right=k
        Sum=float(sum(nums[0:k]))
        maxAvg=Sum/k
        while right<len(nums):
            Sum+=nums[right]
            Sum-=nums[left]
            avg=Sum/k
            if maxAvg<avg:
                maxAvg=avg
            right+=1
            left+=1    
        
        return maxAvg    
             

