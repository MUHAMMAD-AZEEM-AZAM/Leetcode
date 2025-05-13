class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        area=0
   
        for i in range(len(height)):
            h=min(height[start],height[end])
            w=end-start
            new_area= h*w
            if area<new_area:
                area=new_area
            if height[start]<height[end] and start<end:
                start+=1
            else:
                end-=1 
                   
        return area        