class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        q = deque()
        res = []

        for right, num in enumerate(nums):
            #clean tail
            while q and num > nums[q[-1]]:
                q.pop()
            
            #append num index
            q.append(right)

            #clean head
            while q[0] < right - k + 1:
                q.popleft()
            
            if right >= k - 1:
                res.append(nums[q[0]])

        
        return res