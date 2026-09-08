class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0] * len(nums) 
        currentSum = 0
        for i, n in enumerate(nums):
            currentSum += n
            self.prefixSum[i] = currentSum

    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefixSum[left - 1] if left > 0 else 0
        res = self.prefixSum[right] - leftSum

        return res



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)