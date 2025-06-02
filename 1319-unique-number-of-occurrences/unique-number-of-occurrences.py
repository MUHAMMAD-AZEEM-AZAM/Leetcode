class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = {}

        for nums in arr:
            freq_map[nums]=freq_map.get(nums,0)+1
        freq_set  =set()

        for freq in freq_map.values():
            if freq in freq_set:
                return False
            freq_set.add(freq)   
        return True     
