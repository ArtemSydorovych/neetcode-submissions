class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        l = 0
        hashSet = set()

        for r, num in enumerate(nums):
            if (r - l > k):
                hashSet.remove(nums[l])
                l+=1

            if num in hashSet:
                return True

            hashSet.add(num);



        return False