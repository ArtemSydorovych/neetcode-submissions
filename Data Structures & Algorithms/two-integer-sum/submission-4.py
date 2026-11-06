class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i, n in enumerate(nums):
            if target - n in numbers:
                return [numbers[target - n], i]
            numbers[n] = i


        return []