class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""

        for i in range(len(min(strs))):
            element = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != element:
                    return pre
            pre +=  element  
        return pre 

            