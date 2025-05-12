class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=[1]*len(nums)
        count=0
        s=0
        e=len(nums)-1
        for i in range(len(nums)):
            if nums[i]!=0:
                temp[s]=nums[i]
                s+=1
            else:
                temp[e]=0
                e-=1
        for i in range(len(nums)):
            nums[i]=temp[i]           

        # while i<len(nums)-count:
        #     if i>=len(nums):
        #         break
        #     if nums[i] != 0:
        #         temp[i]=nums[i]
        #         i+=1
        #     else:
        #         count+=  1
        # for i in range(count,len(nums)):
        #     temp[i]=0
        # for i in range(len(temp)):
        #     nums[i]=temp[i]



        