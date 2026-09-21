class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1        # mid в левом куске, минимум правее
            else:
                hi = mid            # mid в правом куске, может быть ответом

        return nums[lo]