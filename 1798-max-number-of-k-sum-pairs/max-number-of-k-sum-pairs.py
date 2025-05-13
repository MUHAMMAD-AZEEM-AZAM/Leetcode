class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start=0
        end=len(nums)-1
        operation=0
        nums.sort()
        while start<end:
            if nums[start]+nums[end]==k:
                start+=1
                end-=1
                operation+=1
            elif nums[start]+nums[end] <k:
                start+=1
            else:
                end-=1                     
        return operation        

