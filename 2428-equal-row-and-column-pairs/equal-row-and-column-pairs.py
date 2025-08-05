class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_map = {}

        # Count how many times each row appears (as a tuple)
        for row in grid:
            key = tuple(row)
            row_map[key] = row_map.get(key, 0) + 1

        count = 0
        # For each column, check if its tuple form exists in row_map
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            if col in row_map:
                count += row_map[col]

        return count
