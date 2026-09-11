class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(i, current):
            if i == len(nums):
                res.append(current[::])
                return
            
            current.append(nums[i])
            helper(i + 1, current)
            current.pop()


            helper(i + 1, current)
        
        helper(0, [])
        return res