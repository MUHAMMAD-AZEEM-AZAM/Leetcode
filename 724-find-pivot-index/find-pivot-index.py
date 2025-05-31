class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft=0
        sumRight=sum(nums[1:])
        i=0
        length=len(nums)
        while i<length:
            if sumLeft==sumRight:
                return i
            sumLeft+=nums[i]
            i+=1  
            if i<length:
                sumRight-=nums[i] 
        return -1    
