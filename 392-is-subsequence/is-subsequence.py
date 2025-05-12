class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        lenS=len(s)
        if lenS==0:
            return True
        for i in range(len(t)):
            if j==lenS:
                return True
            if j<lenS and s[j]==t[i]:
                j+=1
        return j>=lenS        
