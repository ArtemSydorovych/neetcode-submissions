class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        curSet = set()

        for r, num in enumerate(nums):
            if num in curSet:
                return True
            curSet.add(num)

            if len(curSet) > k:
                curSet.remove(nums[r - k])
        return False