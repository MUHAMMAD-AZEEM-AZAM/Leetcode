class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        column = [[0 for _ in range(length)] for _ in range(length)]
        count =0
        for i in range(length):
            for j in range(length):
                column[i][j] =grid[j][i]
            
        for col in column:
            for row in grid:
                if col == row:
                    count+=1
        return count        
            