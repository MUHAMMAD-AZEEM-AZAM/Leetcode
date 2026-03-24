class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        e_sum = sum(nums)
        d_sum = 0
        string = "".join(map(str,nums))
        for c in string:
            d_sum += int(c)

        return abs(e_sum - d_sum)   
