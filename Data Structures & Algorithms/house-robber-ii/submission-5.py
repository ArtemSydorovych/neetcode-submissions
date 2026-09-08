from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        @cache
        def max_from(i, flag):
            if (i >= len(nums) or (flag and i == len(nums) - 1)):
                return 0
            
            return max(max_from(i + 1, flag), max_from(i + 2, flag or i == 0) + nums[i])
        
        return max(max_from(0, True), max_from(1, False))