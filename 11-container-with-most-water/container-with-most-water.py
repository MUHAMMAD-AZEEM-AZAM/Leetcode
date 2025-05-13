class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        area=0
        def cal_area():
            h=min(height[start],height[end])
            w=end-start
            return h*w
        area=cal_area()    
        for i in range(len(height)):
            new_area=cal_area()
            if area<new_area:
                area=new_area
            print(area)
            if height[start]<height[end] and start<end:
                start+=1
            else:
                end-=1 
                   
        return area        