class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                check_left= i==0 or flowerbed[i-1]==0
                check_right= i==len(flowerbed)-1 or flowerbed[i+1]==0  
                if check_left and check_right:
                    flowerbed[i]=1
                    total+=1
                if total>=n:
                    return True
        return total>=n                 
           
        