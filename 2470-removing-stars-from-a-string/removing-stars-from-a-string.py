class Solution:
    def removeStars(self, s: str) -> str:
        n = []
        for c in s:
            if c == "*" :
                n.pop()
                continue

            n.append(c)

        return "".join(n)      
        