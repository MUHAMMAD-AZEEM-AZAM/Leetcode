class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans0,ans1=set(nums1),set(nums2)
        return [list(ans0-ans1 ),list(ans1-ans0)]            
        

