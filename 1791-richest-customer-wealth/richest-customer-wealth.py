class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0

        for account in accounts:
            wealth = sum(account)
            if wealth > rich:
                rich = wealth
        return rich    