class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        totalCount=0
        flag=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                flag+=1
            if flowerbed[i]==1:
                flag=0
            if flag==3 or (i==1 and flowerbed[0]==0 and flowerbed[1]==0) or (i==len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0):
                totalCount+=1
                flag=1  
            if totalCount>=n:
                return True     
        return False       
        