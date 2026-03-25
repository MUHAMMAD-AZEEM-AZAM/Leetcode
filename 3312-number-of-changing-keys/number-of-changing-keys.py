class Solution:
    def countKeyChanges(self, s: str) -> int:
        last_key = s[0].lower()
        count = 0
        for i in range(len(s)):
            if last_key == s[i].lower():
                continue
            last_key = s[i].lower()
            count += 1

        return count
