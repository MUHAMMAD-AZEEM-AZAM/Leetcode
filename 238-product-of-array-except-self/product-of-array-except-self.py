class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j=0
        length=len(nums)
        left=[1]*length
        right=[1]*length
        result=[1]*length
        j=0
        for i in range(length):
            if i==0:
                left[i]=1
                continue
            if i==1:    
                left[i]=nums[0]
                continue
            left[i]=nums[i-1]*left[i-1]    
        for i in range(length-1,-1,-1):
            if i==length-1:
                right[i]=1
                continue
            if i==length-2:
                right[i]=nums[i+1]
                continue
            right[i]=nums[i+1]*right[i+1]
        for i in range(length):
            result[i]=left[i]*right[i]    
        return  result

