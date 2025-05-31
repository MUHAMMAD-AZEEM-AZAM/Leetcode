class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i=0
        j=0
        flag=0
        while j<len(nums):
            if nums[j]==0:
                flag+=1
            j+=1    
            if flag>1:
                if nums[i]==0:
                    flag-=1
                i+=1
        return j-i-1        

                
        