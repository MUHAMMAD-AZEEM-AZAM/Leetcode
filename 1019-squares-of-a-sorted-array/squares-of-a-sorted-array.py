class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_array = []
        for i in nums:
            square_array.append(i*i)
        square_array.sort() 
        return square_array
