class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            #if we have first element in res > 0 we won't be able to sum up to 0 at all so we can stop  
            if (n > 0):
                break;
            
            #skip duplicate
            if (i > 0 and n == nums[i - 1]):
                continue

            l, r = i + 1, len(nums) - 1

            while(l < r):
                threeSum = n + nums[l] + nums[r]
                if (threeSum > 0):
                    r -= 1
                if threeSum < 0:
                    l += 1
                if threeSum == 0:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while(nums[l] == nums[l - 1] and l < r):
                        l+= 1
        return res