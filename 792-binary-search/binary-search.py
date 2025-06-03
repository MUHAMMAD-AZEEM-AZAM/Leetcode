class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end=len(nums)-1
        start=0
        while start<=end:
            mid=(end+start)//2
            print(mid)
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                start=mid+1
            else:
                end=mid-1
        return -1        

