class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for n in nums:
            if n>9:
                double += n
            else:
                single += n
        return single != double

        