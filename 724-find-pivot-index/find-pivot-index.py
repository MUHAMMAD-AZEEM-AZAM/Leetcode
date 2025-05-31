class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft=0
        sumRight=sum(nums[1:])
        print(sumRight)
        i=0
        while i<len(nums):
            if sumLeft==sumRight:
                return i
            sumLeft+=nums[i]
            i+=1  
            if i<len(nums):
                sumRight-=nums[i] 
        return -1    
