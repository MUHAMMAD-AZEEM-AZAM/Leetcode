class Solution:
    def reverseVowels(self, s: str) -> str:
        position=[]
        vowelChar=[]
        vowels=['a','e','i','o','u']
        result=[]
        for i in range(len(s)):
            result.append(s[i])
            if s[i].lower() in vowels:
                position.append(i)
                vowelChar.append(s[i])

        vowelChar=vowelChar[::-1]        
        for p in position:
            result[p]=vowelChar.pop(0)
            
        return "".join(result)


