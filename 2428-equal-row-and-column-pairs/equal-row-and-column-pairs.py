from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counter = Counter(tuple(row) for row in grid)
        col_counter = Counter(tuple(col) for col in zip(*grid))
        
        return sum(row_counter[key] * col_counter[key] for key in row_counter)
