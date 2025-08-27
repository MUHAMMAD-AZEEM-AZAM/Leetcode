class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def checkPalindrome(s:str) ->bool:
            start = 0
            end = len(s)-1
            while start<end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if checkPalindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res




