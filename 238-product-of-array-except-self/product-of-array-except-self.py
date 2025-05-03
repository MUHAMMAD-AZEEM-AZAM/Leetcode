class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j=0
        length=len(nums)
        result=[1]*length
        j=0
        for i in range(length):
            if i==0:
                result[i]=1
                continue
            if i==1:    
                result[i]=nums[0]
                continue
            result[i]=nums[i-1]*result[i-1]   
        right=nums[-1]     
        for i in range(length-2,-1,-1):
            result[i]*=right
            right*=nums[i]   
        return  result

