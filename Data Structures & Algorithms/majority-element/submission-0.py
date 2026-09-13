class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxCount = 0
        res = 0
        for key, val in counts.items():
            maxCount = max(val, maxCount)
            if counts[key] >= maxCount:
                res = key

        return res