class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=max(candies)
        result=[]
        for index in range(len(candies)):
            if candies[index]+extraCandies<maximum:
                result.append(False)
            else:
                result.append(True)
        return result            

