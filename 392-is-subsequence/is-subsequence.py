class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        count=0
        if len(s)==0:
            return True
        for i in range(len(t)):
            if j<len(s) and s[j]==t[i]:
                j+=1
                count+=1
        return count>=len(s)        
