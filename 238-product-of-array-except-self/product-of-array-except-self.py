class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        result=[1]*length
        j=0
        result[1]=nums[0]
        for i in range(2,length):
            result[i]=nums[i-1]*result[i-1]   
        right=nums[-1]     
        for i in range(length-2,-1,-1):
            result[i]*=right
            right*=nums[i]   
        return  result

