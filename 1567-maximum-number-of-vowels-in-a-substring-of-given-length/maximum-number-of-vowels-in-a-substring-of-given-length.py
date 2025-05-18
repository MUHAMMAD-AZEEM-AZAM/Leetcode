class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        vowels='aeiou'
        for i in range(k):
            if s[i] in vowels:
                count+=1
        maxm=count 
        i,j=0,k-1
        while j<len(s)-1:
            if s[i] in vowels:
                count-=1
            i+=1
            j+=1
            if s[j] in vowels:
                count+=1  
            if count>maxm:
                maxm=count
        return maxm              