class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
            plants = sum(flowerbed)
            flowerbed = [0] + flowerbed + [0]
            for i in range(1,len(flowerbed)-1):
                if (flowerbed[i-1] + flowerbed[i] + flowerbed[i+1]) == 0 :
                    flowerbed[i] = 1
            return (sum(flowerbed) - plants) >= n  

        