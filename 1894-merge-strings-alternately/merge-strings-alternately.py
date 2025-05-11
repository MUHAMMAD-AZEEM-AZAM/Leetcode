class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new=''
        flag=0
        len1=len(word1)
        len2=len(word2)
        for i in range(min(len1,len2)):
            new=new+word1[i]
            new=new+word2[i]
            flag+=1
        new=new+word1[flag:len1] 
        new=new+word2[flag:len2]   
        return new
