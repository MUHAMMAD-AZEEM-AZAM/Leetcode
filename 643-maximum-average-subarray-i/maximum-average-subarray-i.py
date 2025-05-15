class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        right=k
        maxSum=float(sum(nums[0:k]))
        Sum=maxSum
        while right<len(nums):
            maxSum+=nums[right]
            maxSum-=nums[left]
            if Sum<maxSum:
                Sum=maxSum
            right+=1
            left+=1   
        
        return Sum/k    
             

