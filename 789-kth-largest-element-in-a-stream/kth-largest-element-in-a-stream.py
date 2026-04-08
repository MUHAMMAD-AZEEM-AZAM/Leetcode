class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        index = self.getIndex(val)
        self.nums.insert(index, val)
        return self.nums[-self.k]

    def getIndex(self, val: int) -> int:
        #Binary search
        left, right = 0, len(self.nums)-1
        while left <= right:
            mid = (left + right) // 2
            mid_number = self.nums[mid]

            if val > mid_number:
                left = mid + 1
            elif val < mid_number:
                right = mid-1
            else:
                return mid
        return left
        

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)