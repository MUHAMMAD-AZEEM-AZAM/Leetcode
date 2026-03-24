class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while len(nums)>0:
            alice_n = min(nums)
            nums.remove(alice_n)
            bob_n = min(nums)
            nums.remove(bob_n)

            arr.append(bob_n)
            arr.append(alice_n)
        return arr
