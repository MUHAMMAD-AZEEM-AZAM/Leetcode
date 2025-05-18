class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        vowels='aeiou'
        subString=s[:k]
        for i in subString:
            if i in vowels:
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
            print(i,maxm)    
        return maxm              