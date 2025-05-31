class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes=[0]
        i=0
        while i<len(gain):
            altitudes.append(gain[i]+altitudes[-1])
            i+=1
        return max(altitudes)    
