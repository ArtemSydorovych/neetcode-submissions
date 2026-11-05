class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        curSet = set()
        l = 0

        for r, cur in enumerate(nums):
            if abs(r-l) > k:
                curSet.remove(nums[l])
                l+=1

            if cur in curSet:
                return True

            curSet.add(cur)

        return False

