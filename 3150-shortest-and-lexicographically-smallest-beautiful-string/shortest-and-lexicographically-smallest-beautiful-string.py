class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        all_strings = []
        min_len = float("inf")

        for left in range(n):
            for right in range(left + k, n + 1):
                block = s[left:right]
                if block.count('1') == k:
                    block_len = len(block)
                    if block_len < min_len:
                        min_len = block_len
                        all_strings = [block]
                    elif block_len == min_len:
                        all_strings.append(block)

        if not all_strings:
            return ""

        return min(all_strings)