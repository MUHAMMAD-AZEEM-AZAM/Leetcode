class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_array = []

        for i in arr:
            if i % 2 != 0:
                odd_array.append(i)
            else:
                odd_array = []

            if len(odd_array) == 3:
                return True
        return False    
