class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans0,ans1=set(),set()
        for i in nums1:
            if i not in nums2:
                ans0.add(i)
        for i in nums2:
            if i not in nums1:
                ans1.add(i)    
        return [list(ans0),list(ans1)]            
        

