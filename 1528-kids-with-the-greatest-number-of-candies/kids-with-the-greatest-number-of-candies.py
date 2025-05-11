class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=max(candies)
        result=[]
        for index in range(len(candies)):
            result.append(not candies[index]+extraCandies<maximum)
        return result            

