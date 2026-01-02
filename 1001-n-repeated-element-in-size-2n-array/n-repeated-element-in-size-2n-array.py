class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)/2
        my_map = {}
        for i in nums:
            my_map[f'{i}'] = 0
        for i in nums:
            my_map[f'{i}'] =my_map[f'{i}'] + 1 
            if my_map[f'{i}'] == n:
                return int(i) 
