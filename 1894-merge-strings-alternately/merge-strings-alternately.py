class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1=len(word1)
        len_2=len(word2)
        merged=''
        i=0
        j=0
        
        while i<len_1 and j<len_2:
                merged=merged+word1[i]
                i+=1
                merged=merged+word2[j]
                j+=1
        merged+=word1[i:]  
        merged+=word2[j:]       
        return merged    

