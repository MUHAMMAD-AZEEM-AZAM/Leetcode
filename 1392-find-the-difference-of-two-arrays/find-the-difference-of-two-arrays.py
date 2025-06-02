class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans0,ans1=set(),set()
        for i in nums1:
                ans0.add(i)
        for i in nums2:
                ans1.add(i)    
        diff0=ans0-ans1 
        diff1=ans1-ans0       
        return [list(diff0),list(diff1)]            
        

