class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # expand window until we find subarray sum == target
        # shrink window sum -= nums[left] 
        # expand again to right
        # res = min(minimalSoFar, currentWindowSize)

        res = float('inf')
        left = 0
        curSum = 0

        for right, num in enumerate(nums):
            curSum += num

            while(curSum >= target):
                res = min(right-left + 1, res)
                curSum -= nums[left]
                left += 1

        if res == float('inf'):
            return 0

        
        return res


