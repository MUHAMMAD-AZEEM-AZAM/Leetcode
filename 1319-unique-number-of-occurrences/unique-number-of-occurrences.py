class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = {}

        # Count frequencies
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Check if all frequencies are unique
        freq_set = set()
        for freq in freq_map.values():
            if freq in freq_set:
                return False
            freq_set.add(freq)

        return True