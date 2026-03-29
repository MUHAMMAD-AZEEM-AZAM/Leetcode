class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0

        for account in accounts:
            total = sum(account)
            if total > wealth:
                wealth = total
        return wealth    