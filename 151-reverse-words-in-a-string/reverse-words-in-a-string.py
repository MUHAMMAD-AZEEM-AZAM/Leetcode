class Solution:
    def reverseWords(self, s: str) -> str:
        j=0
        s1=[]
        string=""
        for i in range(len(s)):
            if s[i]==" ":
                s1.append(s[j:i])
                j=i+1
            if  (i==len(s)-1):
                   s1.append(s[j:i+1]) 
        s1=s1[::-1] 
        for i in range (len(s1)):
            if s1[i]!="":
               string=string+s1[i]+" "
        string=string[0:-1]     
        return string       

        