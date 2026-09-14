class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        if len(height) <= 2:
            return 0 
        
        leftMax, rightMax = height[left], height[right]
        res = 0
        
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(height[right], rightMax)
                res += rightMax - height[right]
        return res