class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
       j=0
       for i in range(len(nums)):
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1

        # i=0
        # e=len(nums)-1
        # flag=False
        # while i<=e:
        #     if nums[i]!=0:
        #         i+=1
        #         continue
        #     j=i    
        #     while j<e:
        #         nums[j]=nums[j+1]
        #         if nums[j]==0:
        #             flag=True
        #         j+=1
        #     nums[e]=0
        #     e-=1 
        #     if flag:
        #         i=0
        #     else:
        #         i+=1   






        