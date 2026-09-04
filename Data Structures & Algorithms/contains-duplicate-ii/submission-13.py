class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        seen = set()
        l = 0

        for r, num in enumerate(nums):
            while (r - l > k):
                seen.remove(nums[l])
                l+=1
        
            if num in seen:
                return True
            seen.add(num)


        return False

