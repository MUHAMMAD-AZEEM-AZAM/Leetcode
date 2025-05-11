class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def divides(st,subS):
            if len(st)%len(subS)!=0:
                return False
            n=len(st)//len(subS)    
            return st==n*subS   

        check=0
        minimum=min(len(str1),len(str2))
        for i in range(minimum):
            if str1[i]!=str2[i]:
                break
            check+=1
        subString=str1[0:check]

        for i in range(check):
            if divides(str1,subString) and divides(str2,subString):
                return subString 
            check-=1      
            subString=str1[0:check]

        return ""          


