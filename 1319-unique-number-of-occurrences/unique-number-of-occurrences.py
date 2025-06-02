class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        
        freq = Counter(arr)  # Fast frequency count using hashmap
        return len(set(freq.values())) == len(freq)