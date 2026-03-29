class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_array = 0

        for i in arr:
            if i % 2 != 0:
                odd_array += 1
            else:
                odd_array = 0

            if odd_array == 3:
                return True
        return False    
