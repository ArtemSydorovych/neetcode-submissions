class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def build(i, current):
            if i == len(nums):
                res.append(current[::])
                return

            current.append(nums[i])
            build(i + 1, current)
            current.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i+= 1
            
            build(i + 1, current)

        build(0, [])
        return res

