class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        last_key = s[0]
        count = 0
        for i in range(len(s)):
            if last_key == s[i]:
                continue
            last_key = s[i]
            count += 1

        return count
